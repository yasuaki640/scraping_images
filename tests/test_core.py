import unittest

BASE_URL = 'https://www.instagram.com/explore/tags/'
KEYWORD = '今田美桜'


class GetImagesTest(unittest.TestCase):
    def test_get_soup(self):
        from scrape.core import get_soup
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
