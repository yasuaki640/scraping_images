import requests
from bs4 import BeautifulSoup

hiroshi_res = requests.get('http://abehiroshi.la.coocan.jp/')
hiroshi_res.encoding = 'shift_jis'

hiroshi_html = BeautifulSoup(hiroshi_res.text, 'html.parser')

title = str(hiroshi_html.title.string)
print(hiroshi_html)
