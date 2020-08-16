import requests
from bs4 import BeautifulSoup

ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
url = 'http://abehiroshi.la.coocan.jp/'

hiroshi_res = requests.get(url, headers={'User-Agent': ua})
hiroshi_res.encoding = 'shift_jis'
hiroshi_html = BeautifulSoup(hiroshi_res.text, 'html.parser')

print(hiroshi_html)
