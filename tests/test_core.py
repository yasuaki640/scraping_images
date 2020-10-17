import unittest
import tests.data.data as data

BASE_URL = 'https://www.instagram.com/explore/tags/'
KEYWORD = '今田美桜'
ENCODE = 'utf-8'


class GetImagesTest(unittest.TestCase):
    def test_get_soup(self):
        from scrape.core import get_soup
        soup = get_soup(BASE_URL + '/' + KEYWORD, ENCODE)
        self.assertEqual(True, soup.prettify().__contains__('<!DOCTYPE html>'))

    def test_get_jpg_scrip_tags(self):
        from scrape.core import get_jpg_scrip_tags
        jpg_script_tags = get_jpg_scrip_tags(data.script_tags)

        res = False
        for tag in jpg_script_tags:
            if tag.__contains__('.jpg'):
                res = True

        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
