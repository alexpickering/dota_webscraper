#!/usr/bin/env python3
import scrapy
from scrapy.crawler import CrawlerProcess


class DotaSpider(scrapy.Spider):
    name = 'heroes'
    start_urls = [
            'https://dota2.gamepedia.com/heroes',
            ]

    def parse(self, response):
        #count = 0
        #max   = 3

        for chunk in response.xpath("//div[contains(@id, 'mw-content-text')]//table/tbody/tr/td//a"):
            print(chunk.get())

            href = chunk.xpath('@href').get()
            hero_name = chunk.xpath('@title').get()
            image = chunk.xpath('img/@src').get()
            meta = {
                    "hero": hero_name,
                    "image": image
                   }
            if href:
                yield response.follow(href, self.parse_hero, meta=meta)

        #    count += 1
        #    if count >= max:
        #        break

    def parse_hero(self, response):

        print(f"Parsing page for hero: {response.meta['hero']}")

        for chunk in response.xpath("//table[contains(@class, 'infobox')][1]/tbody"):
            base_chunk = chunk.xpath("tr[1]/th/div[2]")
            if isinstance(base_chunk, list) and len(base_chunk) == 1:
                base_chunk = base_chunk[0]
            else:
                print(len(base_chunk))
                raise Exception

            primary_attribute   = response.xpath("//div[4]/div/p//a[contains(@title, 'Strength') or contains(@title, 'Agility') or contains(@title, 'Intelligence')]/text()").get()

            base_strength       = base_chunk.xpath("div[4]/b/text()").get()
            strength_growth     = base_chunk.xpath("div[4]/text()").get()[3:]
            base_agility        = base_chunk.xpath("div[5]/b/text()").get()
            agility_growth      = base_chunk.xpath("div[5]/text()").get()[3:]
            base_intelligence   = base_chunk.xpath("div[6]/b/text()").get()
            intelligence_growth = base_chunk.xpath("div[6]/text()").get()[3:]

            lvl_chunk = chunk.xpath("tr[2]/td/table/tbody")
            if isinstance(lvl_chunk, list) and len(lvl_chunk) == 1:
                lvl_chunk = lvl_chunk[0]
            else:
                raise Exception

            health = {
                        0 : lvl_chunk.xpath("tr[2]/td[1]/text()").get().strip(),
                        1 : lvl_chunk.xpath("tr[2]/td[2]/text()").get().strip(),
                        15: lvl_chunk.xpath("tr[2]/td[3]/text()").get().strip(),
                        25: lvl_chunk.xpath("tr[2]/td[4]/text()").get().strip(),
                        30: lvl_chunk.xpath("tr[2]/td[5]/text()").get().strip()
                    } 
            health_regen = { 
                        0 : lvl_chunk.xpath("tr[3]/td[1]/text()").get().strip(),
                        1 : lvl_chunk.xpath("tr[3]/td[2]/text()").get().strip(),
                        15: lvl_chunk.xpath("tr[3]/td[3]/text()").get().strip(),
                        25: lvl_chunk.xpath("tr[3]/td[4]/text()").get().strip(),
                        30: lvl_chunk.xpath("tr[3]/td[5]/text()").get().strip()
                    } 
            mana = {
                        0 : lvl_chunk.xpath("tr[4]/td[1]/text()").get().strip(),
                        1 : lvl_chunk.xpath("tr[4]/td[2]/text()").get().strip(),
                        15: lvl_chunk.xpath("tr[4]/td[3]/text()").get().strip(),
                        25: lvl_chunk.xpath("tr[4]/td[4]/text()").get().strip(),
                        30: lvl_chunk.xpath("tr[4]/td[5]/text()").get().strip()
                    } 
            mana_regen = {
                        0 : lvl_chunk.xpath("tr[5]/td[1]/text()").get().strip(),
                        1 : lvl_chunk.xpath("tr[5]/td[2]/text()").get().strip(),
                        15: lvl_chunk.xpath("tr[5]/td[3]/text()").get().strip(),
                        25: lvl_chunk.xpath("tr[5]/td[4]/text()").get().strip(),
                        30: lvl_chunk.xpath("tr[5]/td[5]/text()").get().strip()
                    } 
            armor = {
                        0 : lvl_chunk.xpath("tr[6]/td[1]/text()").get().strip(),
                        1 : lvl_chunk.xpath("tr[6]/td[2]/text()").get().strip(),
                        15: lvl_chunk.xpath("tr[6]/td[3]/text()").get().strip(),
                        25: lvl_chunk.xpath("tr[6]/td[4]/text()").get().strip(),
                        30: lvl_chunk.xpath("tr[6]/td[5]/text()").get().strip()
                    } 
            attacks_per_second = {
                        0 : lvl_chunk.xpath("tr[7]/td[1]/text()").get().strip(),
                        1 : lvl_chunk.xpath("tr[7]/td[2]/text()").get().strip(),
                        15: lvl_chunk.xpath("tr[7]/td[3]/text()").get().strip(),
                        25: lvl_chunk.xpath("tr[7]/td[4]/text()").get().strip(),
                        30: lvl_chunk.xpath("tr[7]/td[5]/text()").get().strip()
                    } 
            damage_low = {
                        0 : lvl_chunk.xpath("tr[8]/td[1]/text()").get().strip().split('‒')[0],
                        1 : lvl_chunk.xpath("tr[8]/td[2]/text()").get().strip().split('‒')[0],
                        15: lvl_chunk.xpath("tr[8]/td[3]/text()").get().strip().split('‒')[0],
                        25: lvl_chunk.xpath("tr[8]/td[4]/text()").get().strip().split('‒')[0],
                        30: lvl_chunk.xpath("tr[8]/td[5]/text()").get().strip().split('‒')[0]
                    }
            damage_high = {
                        0 : lvl_chunk.xpath("tr[8]/td[1]/text()").get().strip().split('‒')[1],
                        1 : lvl_chunk.xpath("tr[8]/td[2]/text()").get().strip().split('‒')[1],
                        15: lvl_chunk.xpath("tr[8]/td[3]/text()").get().strip().split('‒')[1],
                        25: lvl_chunk.xpath("tr[8]/td[4]/text()").get().strip().split('‒')[1],
                        30: lvl_chunk.xpath("tr[8]/td[5]/text()").get().strip().split('‒')[1]
                    } 

            other_stats_chunk = chunk.xpath("tr[3]/td/table/tbody")
            if isinstance(other_stats_chunk, list) and len(other_stats_chunk) == 1:
                other_stats_chunk = other_stats_chunk[0]
            else:
                raise Exception

            magic_resistance           = other_stats_chunk.xpath("tr[1]/td/text()").get().strip()
            movement_speed             = other_stats_chunk.xpath("tr[2]/td/text()").get().strip()
            attack_speed               = other_stats_chunk.xpath("tr[3]/td/text()").get().strip()
            turn_rate                  = other_stats_chunk.xpath("tr[4]/td/text()").get().strip()
            vision_range_day           = other_stats_chunk.xpath("tr[5]/td/span[1]/text()").get()
            vision_range_night         = other_stats_chunk.xpath("tr[5]/td/span[2]/text()").get()
            attack_type                = other_stats_chunk.xpath("tr[6]/td/span/@title").get().strip()
            attack_range               = other_stats_chunk.xpath("tr[6]/td/span/text()").get().strip()
            projectile_speed           = other_stats_chunk.xpath("tr[7]/td/text()").get().strip()
            attack_animation_point     = other_stats_chunk.xpath("tr[8]/td/span[1]/text()").get()
            attack_animation_backswing = other_stats_chunk.xpath("tr[8]/td/span[2]/text()").get()
            base_attack_time           = other_stats_chunk.xpath("tr[9]/td/text()").get().strip()
            damage_block               = other_stats_chunk.xpath("tr[10]/td/text()").get().strip()
            collision_size             = other_stats_chunk.xpath("tr[11]/td/text()").get().strip()
            legs                       = other_stats_chunk.xpath("tr[12]/td/text()").get().strip()
            gib_type                   = other_stats_chunk.xpath("tr[13]/td/text()").get().strip()

            health_set             = DotaSpider.stats_across_levels(health,             name='health')
            health_regen_set       = DotaSpider.stats_across_levels(health_regen,       name='health_regen')
            mana_set               = DotaSpider.stats_across_levels(mana,               name='mana')
            mana_regen_set         = DotaSpider.stats_across_levels(mana_regen,         name='mana_regen')
            armor_set              = DotaSpider.stats_across_levels(armor,              name='armor')
            attacks_per_second_set = DotaSpider.stats_across_levels(attacks_per_second, name='attacks_per_second')
            damage_low_set         = DotaSpider.stats_across_levels(damage_low,         name='damage_low')
            damage_high_set        = DotaSpider.stats_across_levels(damage_high,        name='damage_high')

        yield {
                'hero':                response.meta['hero'],
                # 'image':               response.meta['image'],
                'primary_attribute':   primary_attribute,
                'base_strength':       base_strength,
                'strength_growth':     strength_growth,
                'base_agility':        base_agility,
                'agility_growth':      agility_growth,
                'base_intelligence':   base_intelligence,
                'intelligence_growth': intelligence_growth,
                **health_set,
                **health_regen_set,
                **mana_set,
                **mana_regen_set,
                **armor_set,
                **attacks_per_second_set,
                **damage_low_set,
                **damage_high_set,
                'magic_resistance':           magic_resistance,
                'movement_speed':             movement_speed,
                'attack_speed':               attack_speed,
                'turn_rate':                  turn_rate,
                'vision_range_day':           vision_range_day,
                'vision_range_night':         vision_range_night,
                'attack_type':                attack_type,
                'attack_range':               attack_range,
                'projectile_speed':           projectile_speed,
                'attack_animation_point':     attack_animation_point,
                'attack_animation_backswing': attack_animation_backswing,
                'base_attack_time':           base_attack_time,
                'damage_block':               damage_block,
                'collision_size':             collision_size,
                'legs':                       legs,
                'gib_type':                   gib_type
              }


    @staticmethod
    def stats_across_levels(stat_lookup, name):
        flat = {}

        for lvl in [0, 1, 15, 25, 30]:
            key = name + '_' + str(lvl)
            value = stat_lookup[lvl]
            flat[key] = value

        return flat



def start_crawler(outfile='heroes.csv'):

    process = CrawlerProcess(settings={
        'FEEDS': {
            outfile: {'format': 'csv'},
            },
    })

    process.crawl(DotaSpider)
    process.start()


def main():
    start_crawler()    
    

if __name__ == '__main__':
    main()
