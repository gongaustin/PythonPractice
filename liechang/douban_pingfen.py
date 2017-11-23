import re
import requests
import codecs
import time
import random
from bs4 import BeautifulSoup
absolute = 'https://movie.douban.com/subject/26794215/comments'
absolute_url = 'https://movie.douban.com/subject/26794215/comments?start=20&limit=20&sort=new_score&status=P&percent_type='
url = 'https://movie.douban.com/subject/26794215/comments?start={}&limit=20&sort=new_score&status=P'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0','Connection':'keep-alive'}
def get_data(html):
    soup=BeautifulSoup(html,'lxml')
    comment_list = soup.select('.comment > p')
    commentor_list = soup.select('.comment-info > a')
    next_page= soup.select('#paginator > a')[2].get('href')
    date_nodes = soup.select('..comment-time')
    return comment_list,next_page,date_nodes,commentor_list
if __name__ == '__main__':
    f_cookies = open('cookie.txt', 'r')
    cookies = {}
    for line in f_cookies.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    html = requests.get(absolute_url, cookies=cookies, headers=header).content
    comment_list = []
    # 获取评论
    comment_list, next_page,date_nodes,commentor_list= get_data(html,)
    soup = BeautifulSoup(html, 'lxml')
    comment_list = []
    while (next_page != []):  #查看“下一页”的A标签链接
        print(absolute + next_page)
        html = requests.get(absolute + next_page, cookies=cookies, headers=header).content
        soup = BeautifulSoup(html, 'lxml')
        comment_list, next_page,date_nodes,commentor_list = get_data(html)
        with open("comments.txt", 'a', encoding='utf-8')as f:
            print("comment.size:"+str(len(comment_list)))
            print("date.size:"+str(len(date_nodes)))
            i = 0
            while i < 20:
                comment = comment_list[i].get_text().strip().replace("\n", "")
                date_comment = date_nodes[i].get_text().strip()
                commentor = commentor_list[i].get_text()
                f.writelines((date_comment+' '+commentor+' '+comment) + u'\n')
                i = i + 1

        time.sleep(1 + float(random.randint(1, 100)) / 20)