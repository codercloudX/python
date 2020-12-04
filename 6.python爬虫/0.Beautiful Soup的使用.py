# 安装Beautiful Soup
#   pip3 install bs4 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
from bs4 import BeautifulSoup
import requests
soup=BeautifulSoup("https://www.qiushibaike.com/text/","html.parser")
soup.find('div')


