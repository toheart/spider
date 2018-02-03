# coding:utf-8
import json
import requests
import re
import time

class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"
        headers = {
            "User-Agent": user_agent,
        }
        result = requests.get(url, headers = headers)
        if result.status_code == 200:
            result.encoding = 'utf-8'
            return result.text
        return None


class HtmlParser(object):
    def parser_url(self,page_url, response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls is not None:
            return list(set(urls))
        else:
            return None

    def parser_json(self, page_url, response):
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result is not None:
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e:
                print(e)
                return None
            if isRelease:
                if value.get('value').get('hotValue') == None:
                    return self._parser_release(page_url, value)
                else:
                    return self._parser_no_release(page_url, value, isRelease=2)
            else:
                return self._parser_no_release(page_url, value)

    def _parser_release(self, page_url, value):
        try:
            isRelease = 1
            contentValue = value.get('value')
            movieRating = contentValue.get('movieRating')
            boxOffice = contentValue.get("boxOffice")
            movieTitle = contentValue.get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get("ROtherFinal")
            RatingFinal = movieRating.get('RatingFinal')

            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')

            TotalBoxOffice = boxOffice.get('TotalBoxOffice')
            TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
            TodayBoxOffice = boxOffice.get('TodayBoxOffice')
            TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')

            ShowDays = boxOffice.get('ShowDays')

            try:
                Rank = boxOffice.get("Rank")
            except Exception as e:
                Rank = 0
            return (MovieId,movieTitle,RatingFinal,
                    ROtherFinal, RPictureFinal, RDirectorFinal,
                    RStoryFinal,Usercount, AttitudeCount,
                    TotalBoxOffice+TodayBoxOfficeUnit,
                    TotalBoxOffice+TodayBoxOfficeUnit,
                    Rank, ShowDays, isRelease)
        except Exception as e:
            print(e.page_url, value)
            return None

    def _parser_no_release(self,page_url, value, isRelease=0):
        try:
            contentValue = value.get('value')
            movieRating = contentValue.get('movieRating')
            movieTitle = contentValue.get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get("ROtherFinal")
            RatingFinal = movieRating.get('RatingFinal')
            MovieId = movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount = movieRating.get('AttitudeCount')
            try:
                Rank = value.get('value').get('hotValue').get("Ranking")
            except Exception as e:
                Rank = 0
            return (MovieId,movieTitle,RatingFinal,
                    ROtherFinal, RPictureFinal, RDirectorFinal,
                    RStoryFinal,Usercount, AttitudeCount,
                    u'无', u'无',
                    Rank, 0, isRelease)
        except Exception as e:
            print(e.page_url, value)
            return None