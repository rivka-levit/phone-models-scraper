import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from phone_models.items import PhoneModelItem


class GsmarenaSpider(scrapy.Spider):
    name = "gsmarena"
    allowed_domains = ["gsmarena.com"]
    start_urls = ["https://www.gsmarena.com/makers.php3"]
    rules = (
        Rule(
            LinkExtractor(restrict_xpaths='//div[@class="st-text"]'),
            callback='parse',
            follow=True
        ),
        Rule(
            LinkExtractor(restrict_xpaths='//div[@class="makers"]'),
            callback='parse',
            follow=True
        )
    )

    def parse(self, response, **kwargs):
        pass
