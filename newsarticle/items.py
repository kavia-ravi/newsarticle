# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsarticleItem(scrapy.Item):
    # define the fields for your item here like:
    headline = scrapy.Field()
    article_url = scrapy.Field()
    author = scrapy.Field()
    summary = scrapy.Field()
