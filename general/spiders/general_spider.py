from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from urlparse import urlparse



class GeneralSpider(Spider):
    name = 'general'

    def __init__(self, *args, **kwargs):
        super(GeneralSpider, self).__init__(*args, **kwargs)
        f = open("seeds_es_smp.txt")
        la = [urlparse(url.strip()).netloc for url in f.readlines()]
        f.close()
        self.la = la
        self.le = LinkExtractor()

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return

        for link in self.le.extract_links(response):
            netloc = urlparse(link.url).netloc
            if netloc in self.la:
                r = Request(url=link.url)
                r.meta.update(link_text=link.text)
                yield r

