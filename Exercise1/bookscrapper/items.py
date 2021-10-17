# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscrapperItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    book_stock_availability = scrapy.Field()
    book_star_rating = scrapy.Field()
    book_description = scrapy.Field()
    book_upc = scrapy.Field()
    book_price_excl_tax = scrapy.Field()
    book_price_inc_tax = scrapy.Field()
    book_tax = scrapy.Field()
