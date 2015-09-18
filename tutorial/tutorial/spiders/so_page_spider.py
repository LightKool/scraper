import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from tutorial.pagination import pagination_rule
from tutorial.items import SOQuestionItem

class SOPageSpider(CrawlSpider):
	name = 'StackOverflowPages'
	allowed_domains = ['stackoverflow.com']
	start_urls = ['http://stackoverflow.com/questions/tagged/python']

	rules = (
		Rule(LinkExtractor(allow=('/questions/\d+/.+',), restrict_css=('#questions',)), callback='parse_question'),
		pagination_rule(Rule(LinkExtractor(restrict_xpaths=('.//a[@rel="next"]',)))),
		)

	def parse_question(self, response):
		item = SOQuestionItem()
		m = re.search('/questions/(\d+)/.+', response.url)
		if m:
			item['question_id'] = m.group(1)
		item['question_title'] = response.xpath('.//h1/a/text()').extract_first()
		item['issue_time'] = response.css('span.relativetime').xpath('@title').extract_first()
		yield item