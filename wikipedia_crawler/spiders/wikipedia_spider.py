# -*- coding: utf-8 -*-
import scrapy


class WikipediaSpiderSpider(scrapy.Spider):
    name = 'wikipedia_spider'
    allowed_domains = ['ja.wikipedia.org']
    start_urls = ['https://ja.wikipedia.org/wiki/Wikipedia:ウィキポータル']

    def parse(self, response):
        pass
	#for post in response.css('#mw-content-text'):
        #    # items に定義した Post のオブジェクトを生成して次の処理へ渡す
        #    yield Page(
        #        url=post.css('div.post-header a::attr(href)').extract_first().strip(),
        #        title=post.css('div.post-header a::text').extract_first().strip(),
        #        date=post.css('div.post-header span.date a::text').extract_first().strip(),
        #    )
