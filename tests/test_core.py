import json
import pathlib
import sys
import traceback
import unittest
from tempfile import TemporaryDirectory
import tests.data.data as data

BASE_URL = 'https://www.instagram.com/explore/tags/'
KEYWORD = '今田美桜'
ENCODE = 'utf-8'


class GetImagesTest(unittest.TestCase):

    def setUp(self):
        self.img_dir = TemporaryDirectory()

    def tearDown(self):
        self.img_dir.cleanup()

    def test_get_soup(self):
        from scrape.core import get_soup
        soup = get_soup(BASE_URL + '/' + KEYWORD, ENCODE)
        self.assertTrue(soup.prettify().__contains__('<!DOCTYPE html>'))

    def test_get_jpg_scrip_tags(self):
        from scrape.core import get_jpg_scrip_tags
        script_tags = get_jpg_scrip_tags(data.script_tags)

        contain_jpg = True
        for tag in script_tags:
            if not tag.__contains__('.jpg'):
                contain_jpg = False

        self.assertTrue(contain_jpg)

    def test_get_json_contains_url(self):
        from scrape.core import get_json_contains_url
        str = get_json_contains_url(data.jpg_script_tags)

        result = True

        # Check if the string is in json format
        try:
            json.loads(str)
        except json.JSONDecodeError as e:
            traceback.print_exc(file=sys.stdout)
            result = False

        if not str.__contains__('.jpg'):
            result = False

        self.assertTrue(result)

    def test_download_imgs(self):
        from scrape.core import download_imgs
        download_imgs(KEYWORD, data.img_urls)


if __name__ == '__main__':
    unittest.main()
