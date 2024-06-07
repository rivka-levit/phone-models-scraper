import scrapy


class GsmarenaSpider(scrapy.Spider):
    name = "gsmarena"
    allowed_domains = ["gsmarena.com"]
    start_urls = ["https://gsmarena.com"]

    def parse(self, response, **kwargs):
        pass
