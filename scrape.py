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


url = 'http://abehiroshi.la.coocan.jp/top.htm'
html = get_html(url, 'shift-jis')
img_url = html.find('img')['src']

download_img('http://abehiroshi.la.coocan.jp/abe-top-20190328-2.jpg',
             'C:/Users/yasua/PycharmProjects/scraping_images/img/abe_hiroshi.jpg')

print(img_url)

# やること
# 画像をrequestとか使ってローカルに落とす
# できればopenCVで表示させる
