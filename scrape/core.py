import json
import re
import sys
import traceback

import requests
from bs4 import BeautifulSoup


def main():
    while True:
        keyword = input('Enter keyword of images -->')
        if len(keyword) > 0:
            break

    BASE_URL = 'https://www.instagram.com/explore/tags/'
    soup = get_soup(BASE_URL + keyword, 'utf-8')
    js_scripts = soup.select('script[type="text/javascript"]')
    jpg_jsons = get_jpg_jsons(js_scripts)

    if len(jpg_jsons) <= 0:
        print('No image found.')
        return

    JSON_FILE_PATH = '../url_output/img_paths.json'
    FORMATTED_JSON_FILE_PATH = '../url_output/img_paths_formatted.json'

    format_json_file(jpg_jsons, JSON_FILE_PATH, FORMATTED_JSON_FILE_PATH)

    img_urls = extract_text_in_file(FORMATTED_JSON_FILE_PATH, '"display_url": "', '",')
    download_imgs(keyword, img_urls)
    print(str(len(img_urls)) + ' images downloaded')


def get_soup(url, encode):
    ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    res = requests.get(url, headers={'User-Agent': ua})
    res.encoding = encode
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def get_jpg_jsons(js_scripts):
    jpg_jsons = []

    for script in js_scripts:
        if '.jpg' in str(script):
            jpg_jsons.append(str(script))
    return jpg_jsons


def extract_text_in_file(filepath, pattern_prev, pattern_next):
    extracted_text_array = []
    pattern = pattern_prev + '(.*)' + pattern_next

    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            tmp_extracted_text_array = re.findall(pattern, line)
            extracted_text_array.extend(tmp_extracted_text_array)

    return extracted_text_array


def format_json_file(jpg_jsons, json_file_path, formatted_json_file_path):
    with open(json_file_path, 'w') as js_file:
        jpg_json = jpg_jsons[0].strip('<script type="text/javascript">window._sharedData = ').strip(';</script>')
        js_file.write(jpg_json)

    with open(json_file_path, 'r') as json_file:
        img_path_json = json.load(json_file)

    with open(formatted_json_file_path, 'w') as formatted_json_file:
        json.dump(img_path_json, formatted_json_file, ensure_ascii=True, indent=4, separators=(',', ': '))


def download_imgs(keyword, img_urls):
    for i, url in enumerate(img_urls):
        file_name = keyword + '_' + str(i) + '.jpg'
        path = '../img/' + file_name

        try:
            img = requests.get(url)
            open(path, 'wb').write(img.content)
        except ValueError:
            traceback.print_exc(file=sys.stdout)

        print(file_name + ' downloaded.')


if __name__ == '__main__':
    main()
