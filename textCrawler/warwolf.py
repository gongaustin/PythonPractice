import re
import pandas as pd
import requests

url_first = 'https://movie.douban.com/subject/26363254/comments?start=0'
head = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36'}
cookies = {'cookie': '你自己的cookie'}  # 也就是找到你的账号对应的cookie
html = requests.get(url_first, headers=head, cookies=cookies)

reg = re.compile(r'< a href=" "next">')  # 下一页

ren = re.compile(
    r'<span class="votes">(.*?)</span>.*?comment">(.*?)</ a>.*?</span>.*?<span.*?class="">(.*?)</ a>.*?<span>(.*?)</span>.*?title="(.*?)"></span>.*?title="(.*?)">.*?class=""> (.*?) ',
    re.S)  # 评论等内容

while html.status_code == 200:
    url_next = 'https://movie.douban.com/subject/26363254/comments' + re.findall(reg, html.text)[0]
zhanlang = re.findall(ren, html.text)
data = pd.DataFrame(zhanlang)
data.to_csv('/home/wajuejiprince/文档/zhanlang/zhanlangpinglun.csv', header=False, index=False,
            mode='a+')  # 写入csv文件,'a+'是追加模式
data = []
zhanlang = []
html = requests.get(url_next, cookies=cookies, headers=head)
