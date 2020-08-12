from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://abehiroshi.la.coocan.jp/')
time.sleep(5)
driver.close()
# TODO:何も条件判定せずただ待つだけの
#  よろしくない方法なのでseleniumで書き直す
driver.quit()

