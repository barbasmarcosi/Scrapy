# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy import Field
from scrapy import Item


class RecapcthadataItem(Item):
    image_name = Field()
    image_urls = Field()
    images = Field()


class ImageItem(Item):
    image_urls = Field()
    images = Field()


class MotocyclesItem(Item):
    image_urls = Field()
    images = Field()
