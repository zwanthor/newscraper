# -*- coding: utf-8 -*-

# Scrapy settings for newscraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newscraper'

SPIDER_MODULES = ['newscraper.spiders']
NEWSPIDER_MODULE = 'newscraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newscraper (+http://www.yourdomain.com)'
