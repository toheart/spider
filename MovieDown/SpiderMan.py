#coding:utf-8
from UrlManager import HtmlDownloader,HtmlParser
from DataSave import DataOutput
import urllib

import time

class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        content = self.downloader.download(root_url)
        urls = self.parser.parser_url(root_url, content)
        for url in urls:
            try:
                t = time.strftime("%Y%m%d%H%M%S3282", time.localtime())
                rank_url = "http://service.library.mtime.com/Movie.api?"
                param = {
                    "Ajax_CallBack":True,
                    "Ajax_CallBackType":"Mtime.Library.Services",
                    "Ajax_CallBackMethod":"GetMovieOverviewRating",
                    "Ajax_CrossDomain	": 1,
                    "Ajax_RequestUrl": url[0],
                    "t": t,
                    "Ajax_CallBackArgument0":url[1]
                }
                rank_url = rank_url + urllib.urlencode(param)
                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url, rank_content)
                self.output.store_data(data)
            except Exception as e:
                print("Crawl failed")
            print("Crawl finish")
        self.output.output_end()

if __name__ == "__main__":
    spider = SpiderMan()
    spider.crawl("http://theater.mtime.com/China_Hunan_Province_Zhuzhou")

