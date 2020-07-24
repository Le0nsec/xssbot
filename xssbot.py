#Author:Leon
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import time
import re

chrome_opt = Options()
chrome_opt.binary_location = '/usr/bin/google-chrome-stable'
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--disable-gpu')
chrome_opt.add_argument('--window-size=1366,768')
chrome_opt.add_argument("--no-sandbox")

#Modification
url = "http://ip/xssurllist.php"
cookie1 = {'name':'secret','value':'testxxx','path':'/'}
while 1:
    try:
        browser = webdriver.Chrome(executable_path='/var/xssbot/chromedriver', chrome_options=chrome_opt)
        browser.get(url)
        print('11111')
        s = browser.page_source
        url = re.findall(r"https?://[.0-9]*/",s)[0]
        print(url)
        browser.get(url)
        print('22222')
        browser.add_cookie(cookie1)
        browser.get(url)
        print('ok')
        #print(browser.page_source)
        time.sleep(1)
        browser.quit()
    except Exception as e:
        print (e)
        continue
