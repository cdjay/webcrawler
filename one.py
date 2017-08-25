# 单章小说获取
from urllib.request import urlopen
from bs4 import BeautifulSoup
# 程序开始
url = "http://read.ixdzs.com/154/154938/460922960.html" # 网址
response = urlopen(url) # 打开网址
html = BeautifulSoup(response.read(), 'html.parser') # 以bs4的数据类型赋值html
print(html.title.get_text()) # 获取标题
con = html.find(class_='content') # 获取小说正文
con = con.get_text() # 去除标签
pcon = con.split() # 空格分割正文
for i in range(len(pcon)): #输出小说
    print('')
    print(pcon[i])
