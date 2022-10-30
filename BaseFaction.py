class Merchant:
    starting_wp = 10
    starting_ap = 10

    def __init__(self, start_wp=10, start_ap=10):
        Merchant.starting_wp = start_wp
        Merchant.starting_ap = start_ap
        self.wp_left = start_wp
        self.ap_left = start_ap
        self.faction1: 'Faction' = None
        self.faction2: 'Faction' = None
        self.faction3: 'Faction' = None
        self.revenue = 0

    def assign_factions(self, faction1: 'Faction', faction2: 'Faction', faction3: 'Faction'):
        self.faction1 = faction1
        self.faction2 = faction2
        self.faction3 = faction3

    def sell_weapons(self, faction: 'Faction', ordered_wp):
        flag = False
        if faction not in [self.faction1, self.faction2, self.faction3]:
            print("The faction you want to sell weapons is not in merchant's control")

        elif not faction.is_alive:
            print("“The faction you want to sell weapons is dead!")

        elif ordered_wp > self.wp_left:
            print("You try to sell more weapons than you have in possession.")

        else:
            self.wp_left -= ordered_wp
            self.revenue += ordered_wp
            print("Weapons sold!")
            flag = True
        return flag

    def sell_armors(self, faction: 'Faction', ordered_ap):
        flag = False
        if faction not in [self.faction1, self.faction2, self.faction3]:
            print("The faction you want to sell armors is not in merchant's control")
        elif not faction.is_alive:
            print("“The faction you want to sell armors is dead!")

        elif ordered_ap > self.ap_left:
            print("You try to sell more armors than you have in possession.")

        else:
            self.ap_left -= ordered_ap
            self.revenue += ordered_ap
            print("Armors sold!")
            flag = True
        return flag

    def end_turn(self):
        self.wp_left = Merchant.starting_wp
        self.ap_left = Merchant.starting_ap


class Faction:

    # init method
    def __init__(self, name="Default", no_units=50, attack_pt=30, health_pt=150, unit_rgn=10):
        self.name = name
        self.no_units = no_units
        self.attack_pt = attack_pt
        self.health_pt = health_pt
        self.unit_rgn = unit_rgn
        self.total_health = self.no_units * self.health_pt
        self.is_alive = True
        self.enemy1: 'Faction' = None
        self.enemy2: 'Faction' = None

    def assign_enemies(self, enemy1: 'Faction', enemy2: 'Faction'):
        self.enemy1 = enemy1
        self.enemy2 = enemy2

    def perform_attack(self, no_att_units1, att_pt1, no_att_units2, att_pt2):
        # attacker: 'Faction', attacked: 'Faction'):
        self.enemy1.receive_attack(self, no_att_units1, att_pt1)
        self.enemy2.receive_attack(self, no_att_units2, att_pt2)

    def receive_attack(self, attacker: 'Faction', no_att_units, att_pt):
        self.no_units -= no_att_units * att_pt / self.health_pt
        if self.no_units <= 0:
            self.is_alive = False
            self.no_units = 0
        self.total_health = self.no_units * self.health_pt

    def purchase_weapons(self, merchant: 'Merchant', weapon_pt, coeff_weapon_pt, weapon_price):
        if merchant.sell_weapons(self, weapon_pt):
            self.attack_pt += weapon_pt * coeff_weapon_pt
            return weapon_pt * weapon_price
        return 0

    def purchase_armors(self, merchant: 'Merchant', armors_pt, coeff_armors_pt, armor_price):
        if merchant.sell_armors(self, armors_pt):
            self.health_pt += armors_pt * coeff_armors_pt
            return armors_pt * armor_price
        return 0

    def __str__(self):
        return f"""
                Faction Name:\t{self.name}
                Status:\t{"Alive" if self.is_alive else "Defeated"}
                Number of Units:\t{self.no_units}
                Attack Point:\t{self.attack_pt}
                Health Point:\t{self.health_pt}
                Unit Regen Number:\t{self.unit_rgn}
                Total Faction Health:\t{self.total_health}"""
