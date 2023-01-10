# class="MosaicAsset-module__galleryMosaicAsset____wxTl"
# class="MosaicAsset-module__link___wwW2J"
# response.xpath("//a[@class='MosaicAsset-module__link___wwW2J']").extract()

# class="MosaicAsset-module__figure___qJh1Q"

import scrapy
from motocycles.items import ImageItem
# Título = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
# Next page button = //ul[@class="pager"]//li[@class="next"]/a/@href

# response.xpath("//a[@class='MosaicAsset-module__link___wwW2J']/@href").get()

url = 'https://www.gettyimages.es/fotos/motorcycle'


class QuotesSpider(scrapy.Spider):
    name = 'motorcycles'
    start_urls = [
        url
    ]
    custom_settings = {
        'FEEDS':
            {'motorcycles.json':
                {"format": "json"}
             }
    }

    def url_join(self, rel_img_urls, response):
        joined_urls = []
        for rel_img_url in rel_img_urls:
            joined_urls.append(response.urljoin(rel_img_url))

        return joined_urls

    def parse_images(self, response):
        image = response.xpath(
            "//img[@class='AssetCard-module__image___dams4']/@src").extract()
        item = ImageItem()
        item['image_urls'] = self.url_join(image, response)
        return item

    def parse(self, response):
        count = 1
        maxPagination = int(response.xpath(
            "//span[@class='PaginationRow-module__lastPage___k9Pq7']/text()").get())
        top = getattr(self, 'top', 10)
        if top:
            top = int(top)
        while (count < top and count < maxPagination):
            imagesHrefs = response.xpath(
                "//a[@class='MosaicAsset-module__link___wwW2J']/@href").getall()
            for href in imagesHrefs:
                yield response.follow(href, callback=self.parse_images)
            count += 1
            newImagesUrl = f'{url}?assettype=image&page={count}&phrase=motorcycle&sort=mostpopular&license=rf,rm'
            print(newImagesUrl)
            yield response.follow(newImagesUrl, callback=self.parse)
