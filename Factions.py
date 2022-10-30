from BaseFaction import Faction
class Orcs(Faction):
    """ no __init__() at all here, use the parent's __init__ """

    def perform_attack(self, no_att_units1=0, att_pt1=0, no_att_units2=0, att_pt2=0):
        if self.enemy1.is_alive or self.enemy2.is_alive:
            if self.enemy1.is_alive:
                no_att_units1 = self.no_units
                att_pt1 = self.attack_pt

            if self.enemy2.is_alive:
                no_att_units2 = self.no_units
                att_pt2 = self.attack_pt

            if self.enemy1.is_alive and self.enemy2.is_alive:
                no_att_units1 *= self.no_units * (0.7 if isinstance(self.enemy1, Elves) else 0.3)
                no_att_units2 *= self.no_units * (0.7 if isinstance(self.enemy2, Elves) else 0.3)

        super().perform_attack(no_att_units1, att_pt1, no_att_units2, att_pt2)

    def receive_attack(self, attacker: 'Faction', no_att_units, att_pt):
        att_pt = att_pt * (0.75 if isinstance(attacker, Elves) else 0.80)
        super().receive_attack(attacker, no_att_units, att_pt)

    def purchase_weapons(self, weapon_pt, coeff_weapon_pt, weapon_price):
        super().purchase_weapons(weapon_pt, 2, 20)

    def purchase_armors(self, armors_pt, coeff_armors_pt, armor_price):
        super().purchase_armors(armors_pt, 3, 1)

    def __str__(self):
        return '“Stop running, you’ll only die tired!"\n\n' + super().__str__()


#
class Dwarves(Faction):
    """ no __init__() at all here, use the parent's __init__ """

    def perform_attack(self, no_att_units1=0, att_pt1=0, no_att_units2=0, att_pt2=0):

        if self.enemy1.is_alive or self.enemy2.is_alive:
            if self.enemy1.is_alive:
                no_att_units1 = self.no_units
                att_pt1 = self.attack_pt

            if self.enemy2.is_alive:
                no_att_units2 = self.no_units
                att_pt2 = self.attack_pt

            if self.enemy1.is_alive and self.enemy2.is_alive:
                no_att_units1, no_att_units2 = self.no_units / 2

        super().perform_attack(no_att_units1, att_pt1, no_att_units2, att_pt2)

    def receive_attack(self, attacker: 'Faction', no_att_units, att_pt):
        super().receive_attack(attacker, no_att_units, att_pt)

    def purchase_weapons(self, weapon_pt, coeff_weapon_pt, weapon_price):
        super().purchase_weapons(weapon_pt, 1, 10)

    def purchase_armors(self, armors_pt, coeff_armors_pt, armor_price):
        super().purchase_armors(armors_pt, 2, 3)

    def __str__(self):
        return '"Taste the power of our axes!" \n\n' + super().__str__()


class Elves(Faction):
    """ no __init__() at all here, use the parent's __init__ """

    def perform_attack(self, no_att_units1=0, att_pt1=0, no_att_units2=0, att_pt2=0):

        if self.enemy1.is_alive or self.enemy2.is_alive:
            if self.enemy1.is_alive:
                no_att_units1 = self.no_units
                att_pt1 = self.attack_pt * (1.50 if isinstance(self.enemy1, Dwarves) else 1)

            if self.enemy2.is_alive:
                no_att_units2 = self.no_units
                att_pt2 = self.attack_pt * (1.50 if isinstance(self.enemy2, Dwarves) else 1)

            if self.enemy1.is_alive and self.enemy2.is_alive:
                no_att_units1 *= self.no_units * (0.6 if isinstance(self.enemy1, Orcs) else 0.4)
                no_att_units2 *= self.no_units * (0.6 if isinstance(self.enemy2, Orcs) else 0.4)

        super().perform_attack(no_att_units1, att_pt1, no_att_units2, att_pt2)

    def receive_attack(self, attacker: 'Faction', no_att_units, att_pt):
        att_pt = att_pt * (1.25 if isinstance(attacker, Orcs) else 0.75)
        super().receive_attack(attacker, no_att_units, att_pt)

    def purchase_weapons(self, weapon_pt, coeff_weapon_pt, weapon_price):
        super().purchase_weapons(weapon_pt, 2, 15)

    def purchase_armors(self, armors_pt, coeff_armors_pt, armor_price):
        super().purchase_armors(armors_pt, 4, 5)

    def __str__(self):
        return '"You cannot reach our elegance." \n\n' + super().__str__()


class Merchant:
    starting_wp = 10
    starting_ap = 10
    def __init__(self, start_wp=10, start_ap=10):
        Merchant.starting_wp = start_wp
        Merchant.starting_ap = start_ap
        self.wp_left = self.start_wp
        self.ap_left = self.start_ap
        self.faction1: 'Faction' = None
        self.faction2: 'Faction' = None
        self.faction3: 'Faction' = None
        self.revenue = 0


    def assign_factions(self, faction1: 'Faction', faction2: 'Faction', faction3: 'Faction'):
        self.faction1 = faction1
        self.faction2 = faction2
        self.faction3 = faction3

    def sell_weapons(self, faction: 'Faction', ordered_wp):
        if not faction.is_alive:
            print("“The faction you want to sell weapons is dead!")
            return False

        if ordered_wp > self.wp_left:
            print("You try to sell more weapons than you have in possession.")
            return False

        self.wp_left -= ordered_wp
        print("Weapons sold!")
        return True

    def sell_armors(self, faction: 'Faction', ordered_ap):
        if not faction.is_alive:
            print("“The faction you want to sell armors is dead!")
            return False

        if ordered_ap > self.ap_left:
            print("You try to sell more armors than you have in possession.")
            return False

        self.ap_left -= ordered_ap
        print("Armors sold!")
        return True

    def end_turn(self):
        self.wp_left = Merchant.starting_wp
        self.ap_left = Merchant.starting_ap
