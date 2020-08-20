import requests
from bs4 import BeautifulSoup
import cv2


def get_html(url, encode):
    res = requests.get(url)
    res.encoding = encode
    html = BeautifulSoup(res.text, 'html.parser')
    return html


url = 'http://abehiroshi.la.coocan.jp/top.htm'
html = get_html(url, 'shift-jis')
img_path = html.find('img')['src']

img = requests.get('http://abehiroshi.la.coocan.jp/' + img_path)

print(img_path)

# やること
# 画像をrequestとか使ってローカルに落とす
# できればopenCVで表示させる
