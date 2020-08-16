import requests
import urllib.request
from bs4 import BeautifulSoup

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 ' \
     'Safari/537.36 '
url = 'http://abehiroshi.la.coocan.jp/'
data = None
headers = {'User-Agent': ua}

hiroshi_req = urllib.request.Request(url, data, headers)

hiroshi_res = urllib.request.urlopen(hiroshi_req)
hiroshi_res.encoding = 'shift_jis'
hiroshi_html = BeautifulSoup(hiroshi_res.read(), 'html.parser')

print(hiroshi_html)
