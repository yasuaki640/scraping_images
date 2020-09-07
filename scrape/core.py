import requests
from bs4 import BeautifulSoup
import json
import re
import cv2
import sys, traceback


def main():
    base_url = 'https://www.instagram.com/explore/tags/'
    keyword = input('Enter keyword of images -->')

    soup = get_soup(base_url + keyword, 'utf-8')
    js_scripts = soup.select('script[type="text/javascript"]')
    jpg_jsons = get_jpg_jsons(js_scripts)

    JSON_FILE_PATH = '../url_output/img_paths.json'
    FORMATTED_JSON_FILE_PATH = '../url_output/img_paths_formatted.json'

    format_json_file(jpg_jsons, JSON_FILE_PATH, FORMATTED_JSON_FILE_PATH)

    img_urls = extract_text_in_file(FORMATTED_JSON_FILE_PATH, '"display_url": "', '",')

    for i, url in enumerate(img_urls):
        download_img(url, '../img/' + keyword + '_' + str(i) + '.jpg')


def get_soup(url, encode):
    ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
    res = requests.get(url, headers={'User-Agent': ua})
    res.encoding = encode
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def show_img(file_path, window_name):
    img = cv2.imread(file_path)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


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


def download_img(url, path):
    try:
        img = requests.get(url)
        open(path, 'wb').write(img.content)
    except ValueError:
        print('Value error occured')
        traceback.print_exc(file=sys.stdout)


if __name__ == '__main__':
    main()