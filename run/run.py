from way import re_test
from way.get_pic import *
url_2 = 'https://wallhaven.cc/hot'
driver = webdriver.Chrome()
sr=Get_Pic(driver,url_2)
for i in range(2,20):
    i=str(i)
    url = "https://wallhaven.cc/toplist?page="+i
    linklist = re_test.getlink(url)
    for link in linklist:
        if 'https://wallhaven.cc/w/' in link[0]:
            print(link[0])
            sr.get(link[0])

