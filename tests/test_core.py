import pathlib
import unittest
from tempfile import TemporaryDirectory
import tests.data.data as data

BASE_URL = 'https://www.instagram.com/explore/tags/'
KEYWORD = '今田美桜'
ENCODE = 'utf-8'


class GetImagesTest(unittest.TestCase):

    def setUp(self):
        self.img_dir = TemporaryDirectory()
        self.json_dir = TemporaryDirectory()

    def tearDown(self):
        self.img_dir.cleanup()
        self.json_dir.cleanup()

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

    def test_format_json_file(self):
        from scrape.core import format_json_file
        json_path = pathlib.PurePath(self.json_dir.name + '/img_paths.json')
        formatted_json_path = pathlib.PurePath(self.json_dir.name + '/formatted_img_paths.json')
        format_json_file(data.jpg_script_tags, json_path, formatted_json_path)

    def test_download_imgs(self):
        from scrape.core import download_imgs


if __name__ == '__main__':
    unittest.main()
