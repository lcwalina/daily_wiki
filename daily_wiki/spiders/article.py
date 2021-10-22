import scrapy
from daily_wiki.items import Article

class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    custom_settings = {
        "FEED_FORMAT": "json",
        "FEED_URI": "file:///tmp/%(name)s/%(time)s.json"
    }

    def parse(self, response):
        base_url = 'https://en.wikipedia.org'
        for list in response.css("#mw-content-text > .mw-parser-output > .hlist > ul"):
            for article in list.css("li > span > a") + list.css("li > a"):
                yield Article(
                    title = article.css("::text").get(),
                    link = base_url + article.attrib["href"]
                )

