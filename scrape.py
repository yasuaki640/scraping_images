import requests
from bs4 import BeautifulSoup
import cv2

hiroshi_site_url = 'http://abehiroshi.la.coocan.jp/top.htm'
hiroshi_res = requests.get(hiroshi_site_url)
hiroshi_res.encoding = 'shift_jis'

hiroshi_html = BeautifulSoup(hiroshi_res.text, 'html.parser')

hiroshi_img_path = hiroshi_html.find('img')['src']

download_file_to_dir()

# 画像をダウンロード
hiroshi_img = cv2.imread('http://abehiroshi.la.coocan.jp/abe-top-20190328-2.jpg')

cv2.imshow('阿部寛のご尊顔', hiroshi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# やること
# 画像をrequestとか使ってローカルに落とす
# できればopenCVで表示させる
