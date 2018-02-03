#coding:utf-8
import json
import re
import requests
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
        headers = {"User-Agent": user_agent}
        r = requests.get(url, headers = headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None

class HtmlPaser(object):
    def parser_url(self, page_url, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls != None:
            return list(set(urls))
        else:
            return None

    def parser_json(self, page_url, response):
        pattern = re.compile(r"=(.*?);")
        result = pattern.findall(response)[0]
        if result != None:
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print e
                return None

            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url, value)
                else:
                    return self._parser_no_release(page_url, value, isRelease=2)
            else:
                return self._parser_no_release(page_url, value)


