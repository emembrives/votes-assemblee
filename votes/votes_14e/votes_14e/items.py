# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SimpleVote(scrapy.Item):
    vote_id = scrapy.Field()
    description = scrapy.Field()
    pour = scrapy.Field()
    contre = scrapy.Field()
    abstentions = scrapy.Field()
    details = scrapy.Field()
