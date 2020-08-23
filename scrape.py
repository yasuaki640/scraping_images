import requests
from bs4 import BeautifulSoup
import cv2


def get_html(url, encode):
    res = requests.get(url)
    res.encoding = encode
    html = BeautifulSoup(res.text, 'html.parser')
    return html


def download_img(url, path):
    try:
        img = requests.get(url)
        open(path, 'wb').write(img.content)
    except ValueError:
        print('Value error occured')


def show_img(file_path, window_name):
    img = cv2.imread(file_path)
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


url = 'http://abehiroshi.la.coocan.jp/top.htm'
html = get_html(url, 'shift-jis')
img_file_name = html.find('img')['src']

# TODO pathlibで置換する、imgのurlをもっときれいに取得する
download_img('http://abehiroshi.la.coocan.jp/' + img_file_name,
             'img/' + img_file_name)

show_img('img/' + img_file_name, 'Abe hiroshi\'s face')

# できればopenCVで表示させる
