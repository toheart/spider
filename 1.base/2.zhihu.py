from bs4 import BeautifulSoup
import requests

def zhihuLogin():
    sess = requests.Session()
    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36"}

    html = sess.get("https://www.zhihu.com/signup?next=%2F", headers=headers).text
    print(html)
    bs = BeautifulSoup(html, "lxml")


if __name__ == "__main__":
    zhihuLogin()
