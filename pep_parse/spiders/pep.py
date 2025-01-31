import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        links = response.xpath(
            '//section[@id="numerical-index"]').css('tbody').css('a')
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.xpath(
            '//h1[@class="page-title"]').css('::text').get().split(' – ')
        number = number.split()[1]
        status = response.xpath(
            '//dl[@class="rfc2822 field-list simple"]').css(
                'dt:contains("Status") + dd').css('abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
