"""
Item models for the project.
"""

import scrapy

from itemloaders.processors import Join


class PhoneModelItem(scrapy.Item):
    title = scrapy.Field(output_processor=Join())
    announced = scrapy.Field(output_processor=Join())
