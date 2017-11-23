import urllib.request
import re
import os

#下载图片
def fetch_pictures(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img class="BDE_Image" src="(.*?)" pic_ext="jpeg"  pic_type="0"')
    picture_url_list = r.findall(html_content.decode('utf-8'))

    os.mkdir('liushishi')
    os.chdir(os.path.join(os.getcwd(), 'liushishi'))
    for i in range(len(picture_url_list)):
        picture_name = str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picture_url_list[i], picture_name)
            print("Success to download " + picture_url_list[i])
        except:
            print("Fail to download " + picture_url_list[i])

if __name__ == '__main__':
    fetch_pictures("http://tieba.baidu.com/p/2854146750")