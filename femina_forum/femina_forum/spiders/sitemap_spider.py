import scrapy
from scrapy.spiders import SitemapSpider
from femina_forum.items import ForumItem

class ForumSitemapSpider(SitemapSpider):
    name = "forum_sitemap"
    sitemap_urls = ['https://forum.femina.mk/sitemap.php']
    sitemap_rules = [('/threads', 'parse_threads')]

    def parse_threads(self, response):
        messages = response.css('.message')
        for message in messages:
            item = ForumItem()
            contents = [m.strip() for m in message.css('.messageContent *::text').getall()]
            item['content'] = ''.join([m for m in contents if len(m) > 0])
            item['author'] = message.attrib['data-author']
        yield item

         # Follow pagination links
        next_page = response.css('nav').css('.text::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse_threads)

