from BaseFaction import Faction, Merchant


class Orcs(Faction):
    """ no __init__() at all here, use the parent's __init__ """

    def perform_attack(self, no_att_units1=0, att_pt1=0, no_att_units2=0,
                       att_pt2=0):  # for all factions, all are zero by default, so no attack if conditions aren't satisfied
        if self.enemy1.is_alive or self.enemy2.is_alive:
            if self.enemy1.is_alive:
                no_att_units1 = self.no_units
                att_pt1 = self.attack_pt

            if self.enemy2.is_alive:
                no_att_units2 = self.no_units
                att_pt2 = self.attack_pt

            if self.enemy1.is_alive and self.enemy2.is_alive:
                no_att_units1 = self.no_units * (0.7 if isinstance(self.enemy1, Elves) else 0.3)
                no_att_units2 = self.no_units * (0.7 if isinstance(self.enemy2, Elves) else 0.3)

        super().perform_attack(no_att_units1, att_pt1, no_att_units2, att_pt2)

    def receive_attack(self, attacker: 'Faction', no_att_units, att_pt):
        att_pt = att_pt * (0.75 if isinstance(attacker, Elves) else 0.80)
        super().receive_attack(attacker, no_att_units, att_pt)

    def purchase_weapons(self, merchant: 'Merchant', weapon_pt):
        super().purchase_weapons(merchant, weapon_pt, coeff_weapon_pt=2, weapon_price=20)

    def purchase_armors(self, merchant: 'Merchant', armors_pt):
        super().purchase_armors(merchant, armors_pt, coeff_armors_pt=3, armor_price=1)

    def __str__(self):
        return '“Stop running, you’ll only die tired!"\n' + super().__str__()


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

    def purchase_weapons(self, merchant: 'Merchant', weapon_pt):
        super().purchase_weapons(merchant, weapon_pt, coeff_weapon_pt=1, weapon_price=10)

    def purchase_armors(self, merchant: 'Merchant', armors_pt):
        super().purchase_armors(merchant, armors_pt, coeff_armors_pt=2, armor_price=3)

    def __str__(self):
        return '"Taste the power of our axes!" \n' + super().__str__()


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
                no_att_units1 = self.no_units * (0.6 if isinstance(self.enemy1, Orcs) else 0.4)
                no_att_units2 = self.no_units * (0.6 if isinstance(self.enemy2, Orcs) else 0.4)

        super().perform_attack(no_att_units1, att_pt1, no_att_units2, att_pt2)

    def receive_attack(self, attacker: 'Faction', no_att_units, att_pt):
        att_pt = att_pt * (1.25 if isinstance(attacker, Orcs) else 0.75)
        super().receive_attack(attacker, no_att_units, att_pt)

    def purchase_weapons(self, merchant: 'Merchant', weapon_pt):
        super().purchase_weapons(merchant, weapon_pt, coeff_weapon_pt=2, weapon_price=15)

    def purchase_armors(self, merchant: 'Merchant', armors_pt):
        super().purchase_armors(merchant, armors_pt, coeff_armors_pt=4, armor_price=5)

    def __str__(self):
        return '"You cannot reach our elegance." \n' + super().__str__()
