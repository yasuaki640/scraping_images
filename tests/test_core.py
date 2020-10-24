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

    def test_get_json_contains_url_given_json_as_param(self):
        from scrape.core import get_json_contains_url
        return_str = get_json_contains_url(data.jpg_script_tags)

        is_json = False
        # Check if the string is in json format
        try:
            json.loads(return_str)
            is_json = True
        except json.JSONDecodeError as e:
            traceback.print_exc(file=sys.stdout)

        self.assertEqual(is_json, True)

    def test_get_json_contains_url_given_str_contains_url_as_param(self):
        from scrape.core import get_json_contains_url
        return_str = get_json_contains_url(data.jpg_script_tags)

        contains_jpg = False
        if return_str.__contains__('.jpg'):
            contains_jpg = True

        self.assertTrue(contains_jpg, True)

    def test_download_imgs(self):
        from scrape.core import download_imgs
        download_imgs(KEYWORD, data.img_urls)


if __name__ == '__main__':
    unittest.main()
