from urllib import request


class MovieTop(object):
    def __init__(self):
        self.start = 0
        self.param = '&filter='
        self.headers = {
            'User-Agent': 'Mozilla/5.0(Windows NT6.1;wow64)'
        }

    def get_page(self):
        page_content = []
        try:
            while self.start <= 225:
                url = 'https://movie.douban.com/top250?start=' + str(self.start)
                req = request.Request(url, headers=self.headers)
                response = request.urlopen(req)
                page = response.read().decode('utf-8')
                page_num = (self.start + 25) // 25
                print('Now , get the data of ' + str(page_num) + 'page..')
                self.start += 25
                page_content.append(page)
            return page_content
        except request.URLError as e:
            if hasattr(e,'reason'):
                print('Get failed ,the reason is :' + e.reason)
    def main(self):
        print('Being to get data from douban')
        self.get_page()
        print("End getting")

movieTop = MovieTop()
movieTop.main()
