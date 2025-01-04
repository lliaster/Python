import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse


class Top250Spider(scrapy.Spider):
    name = 'top250'
    # start_urls = ['https://movie.douban.com/top250?start=0&filter=', 'https://movie.douban.com/top250?start=0&filter=']

    def start_requests(self):
        url = 'https://movie.douban.com/top250?start={}&filter='
        for page in range(10):
            # 重写start_requests并将dont_filter设置为false开启过滤
            yield scrapy.Request(url.format(page * 25))


    def parse(self, response: HtmlResponse, **kwargs):
        print('请求头信息:', response.request.headers)


if __name__ == '__main__':
    cmdline.execute('scrapy crawl top250 --nolog'.split())
