import scrapy
from scrapy import Selector

from newsarticle.items import NewsarticleItem

class TheguardianspiderSpider(scrapy.Spider):
    name = 'theguardianspider'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/au',]

    def parse(self, response):
        newsblocks = Selector(response).xpath('//div[@class="fc-item__container"]')
        for news in newsblocks:
            headline = news.xpath('a[@class="u-faux-block-link__overlay js-headline-text"]/text()').extract()[0]
            news_url = news.xpath('a[@class="u-faux-block-link__overlay js-headline-text"]/@href').extract()[0]
            yield response.follow(url=news_url, callback=self.parse_newsurl,meta={'head': headline, 'article_url': news_url})

    def parse_newsurl(self, response):

        item = NewsarticleItem()

        headline = response.request.meta['head']
        articleurl = response.request.meta['article_url']

        newscontent = Selector(response).xpath('/html/body/article/div/div//div')
        paragraph = ""
        for content in newscontent:
            author = content.xpath('//div[@class="dcr-fj5ypv"]//a/text()').extract()[0]
            para = content.xpath('//div/p/text()')
            for lines in para:
               paragraph += lines.extract()
        item['headline'] = headline
        item['article_url'] = articleurl
        item['author'] = author
        item['summary'] = paragraph
        yield item
