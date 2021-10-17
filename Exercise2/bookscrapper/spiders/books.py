# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from urllib.parse import urljoin
import json
import logging
import re
from bookscrapper.items import BookscrapperItem

#BooksSpider class is used to scrape the books in the url books.toscrape.com
class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        urls = [ 'https://books.toscrape.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_book)
            
    #parse_url is used to parse the url and attach the given string       
    def parse_url(self, urlstr):
        url_check = re.search(r'(?<=catalogue/).*', urlstr)
        if url_check:
            attach_str = url_check.group(0)
        else:
            attach_str = urlstr
        return attach_str
    
    #parse_book is used to find the item detail page    
    def parse_book(self, response):
        sel = Selector(response)
        links = sel.xpath('//ol[@class="row"]/li').extract()
        for i in links:
            parse = Selector(text=i)
            book_url = parse.xpath('//article[@class="product_pod"]/h3/a/@href').extract_first()
            suffix_str = self.parse_url(book_url)
            url = urljoin('https://books.toscrape.com/catalogue/', suffix_str)
            yield response.follow(url, callback=self.parse_book_details)
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            suffix2_str = self.parse_url(next_page)
            url = urljoin('https://books.toscrape.com/catalogue/', suffix2_str)
            yield response.follow(url, callback=self.parse_book)
   
    #parse_book_details is used to find the attributes of book in detail page
    def parse_book_details(self, response):
        item = BookscrapperItem()
        item['book_name'] = response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
        item['book_price'] = response.xpath('//p[@class="price_color"]/text()').get()
        item['book_stock_availability'] = response.xpath('//i[@class="icon-ok"]/following-sibling::text()').get().strip()
        star_rating = response.css('.star-rating').xpath("@class").extract()
        for cls in star_rating:
            match = re.search(r'(?<=star-rating).*', cls)
            if match:
                item['book_star_rating']=match.group(0)
            else:
                item['book_star_rating']=0
        item['book_description'] = response.xpath('//*[@id="content_inner"]/article/p/text()').get()
        item['book_upc'] = response.xpath('//table[@class="table table-striped"]/tr[1]/td/text()').extract_first()
        item['book_price_excl_tax'] = response.xpath('//table[@class="table table-striped"]/tr[3]/td/text()').extract_first()
        item['book_price_inc_tax'] = response.xpath('//table[@class="table table-striped"]/tr[4]/td/text()').extract_first()
        item['book_tax'] = response.xpath('//table[@class="table table-striped"]/tr[5]/td/text()').extract_first()
        logging.info('scraped items are...{}'.format(item))
        yield item
        
