import requests
from bs4 import BeautifulSoup

hiroshi_res = requests.get('http://abehiroshi.la.coocan.jp/top.htm')
hiroshi_res.encoding = 'shift_jis'

hiroshi_html = BeautifulSoup(hiroshi_res.text, 'html.parser')

print(hiroshi_html.find('img')['src'])


