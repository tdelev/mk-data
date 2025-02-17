from scrapy.spiders import SitemapSpider
from femina_forum.items import ForumItem

class FeminaSpider(SitemapSpider):
    name = "femina"
    sitemap_urls = ['https://forum.femina.mk/sitemap.php']
    sitemap_rules = [('/threads', 'parse_threads')]

    def parse_threads(self, response):
        url = response.url
        parts = response.url.split('page-')
        if len(parts) > 1:
            page = int(parts[-1])
        else:
            page = 1
        messages = response.css('.message')
        topic = response.css('.titleBar h1::text').get()
        for i, message in enumerate(messages):
            item = ForumItem()
            contents = [m.strip() for m in message.css('.messageContent *::text').getall()]
            item['content'] = ' '.join([m for m in contents if len(m) > 0]).strip()
            item['author'] = message.attrib['data-author']
            item['topic'] = topic
            item['time'] = message.css('.DateTime').attrib['title']
            item['url'] = response.url
            item['index'] = (page - 1) * 10 + (i + 1)
            yield item

         # Follow pagination links
        next_page = response.xpath("//a[contains(., 'Следна')]")
        if next_page:
            url = next_page.attrib['href']
            if url:
                yield response.follow(url, self.parse_threads)

