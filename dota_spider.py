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

        for chunk in response.xpath("/html/body/div[2]/div[3]/div[1]/div[3]/div[4]/div/table[1]/tbody"):
            base_chunk = chunk.xpath("tr[1]/th/div[2]")
            if isinstance(base_chunk, list) and len(base_chunk) == 1:
                base_chunk = base_chunk[0]
            else:
                raise Exception
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
            damage = {
                        0 : lvl_chunk.xpath("tr[8]/td[1]/text()").get().strip(),
                        1 : lvl_chunk.xpath("tr[8]/td[2]/text()").get().strip(),
                        15: lvl_chunk.xpath("tr[8]/td[3]/text()").get().strip(),
                        25: lvl_chunk.xpath("tr[8]/td[4]/text()").get().strip(),
                        30: lvl_chunk.xpath("tr[8]/td[5]/text()").get().strip()
                    } 

            other_stats_chunk = chunk.xpath("tr[3]/td/table/tbody")
            if isinstance(other_stats_chunk, list) and len(other_stats_chunk) == 1:
                other_stats_chunk = other_stats_chunk[0]
            else:
                raise Exception
            magic_resistance = other_stats_chunk.xpath("tr[1]/td/text()").get().strip()
            movement_speed = other_stats_chunk.xpath("tr[2]/td/text()").get().strip()
            attach_speed = other_stats_chunk.xpath("tr[3]/td/text()").get().strip()
            turn_rate = other_stats_chunk.xpath("tr[4]/td/text()").get().strip()
            vision_range = "(Day/Night): " + \
                other_stats_chunk.xpath("tr[5]/td/span[1]/text()").get() + "/" + \
                other_stats_chunk.xpath("tr[5]/td/span[2]/text()").get()
            attack_range = other_stats_chunk.xpath("tr[6]/td/span/@title").get().strip() + \
                    ": " + other_stats_chunk.xpath("tr[6]/td/span/text()").get().strip()
            projectile_speed = other_stats_chunk.xpath("tr[7]/td/text()").get().strip()
            attack_animation = "(Atk Point/Atk Backswing): " + \
                other_stats_chunk.xpath("tr[8]/td/span[1]/text()").get() + "+" + \
                other_stats_chunk.xpath("tr[8]/td/span[2]/text()").get() 
            base_attack_time = other_stats_chunk.xpath("tr[9]/td/text()").get().strip()
            damage_block = other_stats_chunk.xpath("tr[10]/td/text()").get().strip()
            collision_size = other_stats_chunk.xpath("tr[11]/td/text()").get().strip()
            legs = other_stats_chunk.xpath("tr[12]/td/text()").get().strip()
            gib_type = other_stats_chunk.xpath("tr[13]/td/text()").get().strip()

            health_set = DotaSpider.stats_across_levels(health, name='health')
            health_regen_set = DotaSpider.stats_across_levels(health_regen, name='health_regen')



        yield {
                'hero': response.meta['hero'],
                'image': response.meta['image'],
                'base_strength': base_strength,
                'strength_growth': strength_growth,
                'base_agility': base_agility,
                'agility_growth': agility_growth,
                'base_intelligence': base_intelligence,
                'intelligence_growth': intelligence_growth,
                **health_set,
                **health_regen_set,
                # TODO(apick): add other lvl-dependent stats on 129 and below

                #'health_0': health[0],
                #'health_1': health[1],
                #'health_15': health[15],
                #'health_25': health[25],
                #'health_30': health[30],
                #'health_regen': health_regen,
                #'mana': mana,
                #'mana_regen': mana_regen,
                #'armor': armor,
                #'attacks_per_second': attacks_per_second,
                #'damage': damage,

                'magic_resistance': magic_resistance,
                'movement_speed': movement_speed,
                'attach_speed': attach_speed,
                'turn_rate': turn_rate,
                'vision_range': vision_range,
                'attack_range': attack_range,
                'projectile_speed': projectile_speed,
                'attack_animation': attack_animation,
                'base_attack_time': base_attack_time,
                'damage_block': damage_block,
                'collision_size': collision_size,
                'legs': legs,
                'gib_type': gib_type
              }


    @staticmethod
    def stats_across_levels(stat_lookup, name):
        flat = {}

        for lvl in [0, 1, 15, 25, 30]:
            key = name + '_' + str(lvl)
            value = stat_lookup[lvl]
            flat[key] = value

        return flat
