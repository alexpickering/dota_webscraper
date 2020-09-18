import copy

class Hero(object):
    ROUND = {
            'strength': 1,
            'intelligence': 1
            }

    DEFAULT_DICT_KEYS = {
            }


    def __init__(self, *args, **kwargs):
        self.name                = kwargs['hero']
        self.primary             = kwargs['primary_attribute']

        self.strength_base       = float(kwargs['base_strength'])
        self.strength_growth     = float(kwargs['strength_growth'])

        self.agility_base        = float(kwargs['base_agility'])
        self.agility_growth      = float(kwargs['agility_growth'])

        self.intelligence_base   = float(kwargs['base_intelligence'])
        self.intelligence_growth = float(kwargs['intelligence_growth'])

        self.health_base       = float(kwargs['health_0'])
        self.health_regen_base = float(kwargs['health_regen_0'])

        self.mana_base         = float(kwargs['mana_0'])
        self.mana_regen_base   = float(kwargs['mana_regen_0'])

        self.armor_base        = float(kwargs['armor_0'])

        self.attack_speed      = float(kwargs['attack_speed'])
        self.base_attack_time  = float(kwargs['base_attack_time'])

        self.damage_low_base   = float(kwargs['damage_low_0'])
        self.damage_high_base  = float(kwargs['damage_high_0'])

        self.level = 1

   #     self.primary_count = self.get_primary_count

   # def get_primary_count(self):
   #     primary = self.primary
   #     if primary=='strength':
   #         return self.strength
   #     elif primary=='agility':
   #         return self.agility
   #     elif primary=='intelligence':
   #         return self.intelligence
   #     else:
   #         raise Exception


    @property
    def strength(self):
        return self.strength_base + (self.strength_growth * self.level)

    @property
    def agility(self):
        return self.agility_base + (self.agility_growth * self.level)

    @property
    def intelligence(self):
        return self.intelligence_base + (self.intelligence_growth * self.level)

    @property
    def attribute_total(self):
        return self.strength + self.agility + self.intelligence

    @property
    def health(self):
        return self.health_base + (self.strength * 20)

    @property
    def health_regen(self):
        return self.health_regen_base + (0.1 * self.strength)

    @property
    def mana(self):
        return self.mana_base + (12 * self.intelligence)

    @property
    def mana_regen(self):
        return self.mana_regen_base + (0.05 * self.intelligence)

    @property
    def armor(self):
        return self.armor_base + ((1.0/6) * self.agility)

    @property
    def attacks_per_second(self):
        return (self.attack_speed + self.agility * 0.01) / self.base_attack_time

    @property
    def damage_low(self):
        return self.damage_low_base + self.primary_attribute_value

    @property
    def damage_high(self):
        return self.damage_high_base + self.primary_attribute_value

    @property
    def primary_attribute_value(self):
        return getattr(self, self.primary)



    def to_dict(self, title_case=False, rounded=False):
        ret = copy.deepcopy(self.__dict__)

        # Get a list of the property names ['strength', 'agility', 'intelligence']
        property_names=[p for p in dir(__class__) if isinstance(getattr(__class__,p),property)]
        # For each property, get its value using getattr() -- put that in our dict
        for p in property_names:
            ret[p] = getattr(self,p)

        if rounded:
            keys_to_round = set(self.__class__.ROUND.keys()) & set(ret.keys())
            for r in keys_to_round:
                ret[r] = round(ret[r], self.__class__.ROUND[r])

        # Change key case last, otherwise we'll forget what to call things
        if title_case:
            keys = list(ret.keys())
            for key in keys:
                ret[key.replace('_',' ').title()] = ret.pop(key)

        return ret
