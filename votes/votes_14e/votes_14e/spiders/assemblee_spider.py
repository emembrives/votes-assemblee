import scrapy

from votes_14e.items import SimpleVote

class AssembleeSpider(scrapy.Spider):
    name = "assemblee"
    allowed_domains = ["assemblee-nationale.fr"]
    start_urls = [
        "http://www2.assemblee-nationale.fr/scrutins/liste/%28legislature%29/14"
    ]

    def parse(self, response):
        nextpage = response.xpath('//div[contains(@class, "pagination-right")][last()]/ul/li[last()][not(contains(@class, "active"))]/a/@href').extract()
        if len(nextpage) != 0:
            url = response.urljoin(nextpage[0])
            yield scrapy.Request(url, callback=self.parse)
        for sel in response.xpath('//table[contains(@class,"scrutins")]//tr'):
            item = SimpleVote()
            item['vote_id'] = sel.xpath('td[contains(@class,"denom")]/text()').extract()
            item['description'] = sel.xpath('td[contains(@class,"desc")]/text()[1]').extract()
            item['details'] = sel.xpath('td[contains(@class,"desc")]/a[last()]/@href').extract()
            item['pour'] = sel.xpath('td[contains(@class,"pour")]/text()').extract()
            item['contre'] = sel.xpath('td[contains(@class,"contre")]/text()').extract()
            item['abstentions'] = sel.xpath('td[contains(@class,"abs")]/text()').extract()
            yield item
