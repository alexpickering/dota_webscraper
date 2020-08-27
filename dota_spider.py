import scrapy

class DotaSpider(scrapy.Spider):
    name = 'heroes'
    start_urls = [
            'https://dota2.gamepedia.com/heroes',
            ]

    def parse(self, response):
        count = 0
        max   = 3

        for chunk in response.xpath("//div[contains(@id, 'mw-content-text')]//table/tbody/tr/td//a"):
            print(chunk.get())

            #yield {
            #        'hero': chunk.xpath('@title').get(),
            #        'link': chunk.xpath('@href').get(),
            #        }
            href = chunk.xpath('@href').get()
            hero_name = chunk.xpath('@title').get()
            image = chunk.xpath('img/@src').get()
            meta = {
                    "hero": hero_name,
                    "image": image
                   }
            if href:
                yield response.follow(href, self.parse_hero, meta=meta)

            count += 1
            if count >= max:
                break

    def parse_hero(self, response):
        print("DIFFERENT RESPONSE START")
        print(response)
        print(response.meta)
        print("DIFFERENT RESPONSE END")

        #strength = response.xpath("strength").get()

        strength = 1
        agility = 1


        yield {
                'hero': response.meta['hero'],
                'image': response.meta['image'],
                'strength': strength,
                'agility': agility,
              }

