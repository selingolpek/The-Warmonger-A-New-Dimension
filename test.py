import BaseFaction
import Factions

Orcs = Factions.Orcs(name="Orcs", no_units=40, attack_pt=100, health_pt=150, unit_rgn=10)
Dwarves = Factions.Dwarves(name="Dwarves")  # has default attr.
Elves = Factions.Elves(name="Elves", no_units=100, attack_pt=20, health_pt=200, unit_rgn=10)

Orcs.assign_enemies(Elves, Dwarves)
Elves.assign_enemies(Dwarves, Orcs)
Dwarves.assign_enemies(Elves, Orcs)

Merchant = BaseFaction.Merchant()  # no argument given
Merchant.assign_factions(Orcs, Elves, Dwarves)

print("\nORCS STATUS:", Orcs, sep="\n\n", end="\n\n")

print("DWARVES AND ELVES BEFORE ATTACK\n")
print(Dwarves, Elves, sep="\n\n", end="\n\n")
Orcs.perform_attack()
print("DWARVES AND ELVES AFTER ATTACK\n")
print(Dwarves, Elves, sep="\n\n", end="\n\n")

print("BEFORE PURCHASING WEAPONS AND ARMORS:", Orcs, end="\n\n", sep="\n\n")
Orcs.purchase_weapons(Merchant, weapon_pt=7)
Orcs.purchase_armors(Merchant, armors_pt=10)
print("\nAFTER PURCHASE:", Orcs, end="\n", sep="\n\n")
print("\nTRY PURCHASING AGAIN\n")
Orcs.purchase_weapons(Merchant, weapon_pt=7)
print()

print("DWARVES AND ELVES BEFORE ATTACK\n")
print(Dwarves, Elves, sep="\n\n", end="\n\n")
Orcs.perform_attack()
print("DWARVES AND ELVES AFTER ATTACK\n")
print(Dwarves, Elves, sep="\n\n", end="\n\n")
