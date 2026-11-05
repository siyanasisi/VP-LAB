import random

def simulate_combat_round(attacker, defender):
    damage = attacker["attack"]

    if random.random() < attacker["crit_chance"]:
        damage *= 2
        attack_type = "Critical hit!"
    else:
        attack_type = "Normal hit."

    damage = max(0, damage - defender["defense"])

    if damage > defender["hp"]:
        damage = defender["hp"]
    defender["hp"] -= damage

    if defender["hp"] <= 0:
        status = defender["name"] + " has been defeated!"
    elif damage == 0:
        status = defender["name"] + " takes no damage."
    else:
        status = defender["name"] + " has been hit."

    report = (
        attacker["name"] + " attacks " + defender["name"] + ". "
        + attack_type + " "
        + "Damage dealt: " + str(damage) + ". "
        + status + " "
        + "Remaining HP: " + str(defender["hp"])
    )

    return report, defender

attacker = {
    "name": "Warrior",
    "hp": 100,
    "attack": 30,
    "defense": 5,
    "crit_chance": 0.25
}
defender = {
    "name": "Goblin",
    "hp": 50,
    "attack": 15,
    "defense": 10,
    "crit_chance": 0.10
}

report, defender = simulate_combat_round(attacker, defender)
print(report)
print(defender)
