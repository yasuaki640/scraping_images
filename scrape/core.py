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
    script_tags = soup.select('script[type="text/javascript"]')
    jpg_script_tags = get_jpg_scrip_tags(script_tags)

    if len(jpg_script_tags) <= 0:
        print('No image found.')
        return

    JSON_FILE_PATH = '../url_output/img_paths.json'
    FORMATTED_JSON_FILE_PATH = '../url_output/img_paths_formatted.json'

    format_json_file(jpg_script_tags, JSON_FILE_PATH, FORMATTED_JSON_FILE_PATH)

    img_urls = extract_str_in_file(FORMATTED_JSON_FILE_PATH, '"display_url": "', '",')
    download_imgs(keyword, img_urls)
    print(str(len(img_urls)) + ' images downloaded')


def get_soup(url, encode):
    ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    res = requests.get(url, headers={'User-Agent': ua})
    res.encoding = encode
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def get_jpg_scrip_tags(script_tags):
    jpg_script_tags = []

    for script_tag in script_tags:
        if '.jpg' in str(script_tag):
            jpg_script_tags.append(str(script_tag))
    return jpg_script_tags


def extract_str_in_file(file_path, pattern_prev, pattern_next):
    extracted_strings = []
    pattern = pattern_prev + '(.*)' + pattern_next

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            extracted_str = re.findall(pattern, line)
            extracted_strings.extend(extracted_str)

    return extracted_strings


def format_json_file(jpg_script_tag, json_file_path, formatted_json_file_path):
    with open(json_file_path, 'w') as json_file:
        img_path_json = jpg_script_tag[0].strip('<script type="text/javascript">window._sharedData = ').strip(';</script>')
        json_file.write(img_path_json)

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
