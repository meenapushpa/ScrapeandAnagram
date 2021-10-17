# -*- coding: utf-8 -*-

# Scrapy settings for bookscrapper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bookscrapper'

SPIDER_MODULES = ['bookscrapper.spiders']
NEWSPIDER_MODULE = 'bookscrapper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookscrapper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'random_useragent.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware':None,
    'bookscrapper.middlewares.RetryMiddleware':200,
    'bookscrapper.middlewares.BookscrapperSpiderMiddleware':100,
    'bookscrapper.middlewares.ProxyMiddleware':100,
}
USER_AGENT_LIST = "/root/bookscrapper/bookscrapper/useragents.txt"

LOG_LEVEL='INFO'
LOG_LEVEL='DEBUG'

CONCURRENT_REQUESTS = 5
CONCURRENT_REQUESTS_PER_DOMAIN = 5

DOWNLOAD_TIMEOUT = 60
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True

RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 404, 408]

REDIRECT_ENABLED = True
REFERER_ENABLED = False

COOKIES_ENABLED = False
COOKIES_DEBUG = False
