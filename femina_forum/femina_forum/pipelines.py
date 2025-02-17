# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FeminaForumPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        # Sort items based on a specific field, e.g., 'date'
        self.items.sort(key=lambda x: (x['topic'], x['index']))
        for i in self.items:
            print('Item: ', i)


    
