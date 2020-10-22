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
    ENCODE = 'utf-8'
    soup = get_soup(BASE_URL + keyword, ENCODE)

    script_tags = soup.select('script[type="text/javascript"]')
    jpg_script_tags = get_jpg_scrip_tags(script_tags)

    if len(jpg_script_tags) <= 0:
        print('No image found.')
        return

    img_url_json = get_json_contains_url(jpg_script_tags)
    img_urls = extract_str(img_url_json, '"display_url": "', '",')

    DESTINATION_DIR = '../img/'
    count = download_imgs(keyword, img_urls, DESTINATION_DIR)
    print(str(count) + ' images downloaded')


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


def extract_str(original_str, pattern_prev, pattern_next):
    extracted_strings = []
    pattern = pattern_prev + '(.*)' + pattern_next

    members = original_str.splitlines()
    for member in members:
        extracted_str = re.findall(pattern, member)
        extracted_strings.extend(extracted_str)

    return extracted_strings


def get_json_contains_url(jpg_script_tag):
    img_path_json_str = jpg_script_tag[0] \
        .strip('<script type="text/javascript">window._sharedData = ') \
        .strip(';</script>')
    dict_data = json.loads(img_path_json_str)

    return json.dumps(dict_data, ensure_ascii=True, indent=4)


def download_imgs(keyword, img_urls, destination_dir):
    num_of_imgs = 0
    for i, url in enumerate(img_urls):
        file_name = keyword + '_' + str(i) + '.jpg'
        path = destination_dir + file_name
        img = requests.get(url)

        with open(path, 'wb') as f:
            f.write(img.content)
            num_of_imgs = num_of_imgs + 1
            print(file_name + ' downloaded.')

    return num_of_imgs


if __name__ == '__main__':
    main()
