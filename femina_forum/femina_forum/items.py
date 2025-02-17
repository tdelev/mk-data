# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ForumItem(scrapy.Item):
    content = scrapy.Field()
    topic = scrapy.Field()
    author = scrapy.Field()
    index = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()

