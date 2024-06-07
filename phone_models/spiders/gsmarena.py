"""
Spider for gsmarena site. Extracts all phone models from the site.
"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

from phone_models.items import PhoneModelItem


class GsmarenaSpider(CrawlSpider):  # noqa
    name = "gsmarena"  # noqa
    allowed_domains = ["gsmarena.com"]  # noqa
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
        item = ItemLoader(
            PhoneModelItem(),
            response=response,
            selector=response
        )
        item.add_xpath(
            'title',
            './/h1[@class="specs-phone-name-title"]/text()'
        )
        item.add_xpath(
            'announced',
            './/div[@id="specs-list"]/table[2]//tr[1]/td[2]/text()'
        )

        yield item.load_item()
