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

        if self.no_units == 0:
            self.is_alive = False

    def purchase_weapons(self, weapon_pt, coeff_weapon_pt, weapon_price):
        self.attack_pt += weapon_pt * coeff_weapon_pt
        return weapon_pt * weapon_price

    def purchase_armors(self, armors_pt, coeff_armors_pt, armor_price):
        self.health_pt += armors_pt * coeff_armors_pt
        return armors_pt * armor_price

    def __str__(self):
        return f"""
                Faction Name:\t{self.name}
                Status:\t{"Alive" if self.is_alive else "Defeated"}
                Number of Units:\t{self.no_units}
                Attack Point:\t{self.attack_pt}
                Health Point:\t{self.health_pt}
                Unit Regen Number:\t{self.unit_rgn}
                Total Faction Health:\t{self.total_health}
        """
