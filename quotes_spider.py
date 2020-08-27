import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
            'http://quotes.toscrape.com/tag/humor/',
            ]

    def parse(self, response):
        # For each chunk
        for chunk in response.xpath("//div[contains(@class, 'quote')]"):
            print("QUOTE IS HAPPENING")
            print(type(chunk))
            print(chunk)
            print(chunk.get())
            print("QUOTE IS OVERRRRRR")
            yield {
                    'author': chunk.xpath('span/small/text()').get(),
                    'text': chunk.xpath("span[contains(@class, 'text')]/text()").get()
                  }

            next_page_url = response.xpath("//li[@class='next']/a/@href").get()
            print(f"next page url: {next_page_url}")
            if next_page_url:
                yield response.follow(next_page_url, self.parse_differently)


        #for quote in response.css('div.quote'):
        #    yield {
        #            'author': quote.xpath('span/small/text()').get(),
        #            'text': quote.xpath("span[contains(@class, 'text')]/text()").get(),
        #            }
        #    next_page = response.css('li.next a::attr("href")').get()
        #    if next_page is not None:
        #        yield response.follow(next_page, self.parse)

    def parse_differently(self, response):
        print("DIFFERENT RESPONSE START")
        print(response)
        print("DIFFERENT RESPONSE END")


