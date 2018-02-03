import urllib2

import re


class Spider:
    def __init__(self):
        self.page = 1
        self.switch = True


    def loadPage(self,page):
        """ download html"""
        url = "http://www.isocialkey.com/article/list_5_"+ str(page) +".html"
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

        html = response.read().decode('GBK')
#       print(html)
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>',re.S)
        content_list = pattern.findall(html)
#        print(content_list)
        for content in content_list:
            print(content)
        self.dealPage(content_list)

    def dealPage(self,content_list):
        for item in content_list:
            item = item.replace("<p>","").replace("</p>","").replace("<br />","")
            print(item)

    


    def writePage(self):
        pass

    def startWork(self):
        pass


if __name__ == "__main__":
    mytest = Spider()
    mytest.loadPage(1)
