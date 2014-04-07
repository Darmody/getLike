# Scrapy settings for getLikeScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'getLikeScrapy'

SPIDER_MODULES = ['getLikeScrapy.spiders']
NEWSPIDER_MODULE = 'getLikeScrapy.spiders'

# Setting up django's project full path.
import sys
sys.path.insert(0, 'D:/workspace/python/django/getLikeWeb')

# Setting up django's settings module name.
# This module is located at /home/rolando/projects/myweb/myweb/settings.py.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'getLikeWeb.settings'

ITEM_PIPELINES = {
    'getLikeScrapy.pipelines.GetDramaPipeline': 1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'getLikeScrapy (+http://www.yourdomain.com)'

