# TH 2nd Conditionals Notes
import random
monster_hp = 30
dmg_modifier = 2
atck_bonus = 3
player_hp = 25

roll = random.randint(1,20)    
if roll == 20:
    print(f"You rolled a crit, double your damage.")
    attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll + atck_bonus > 10:
    print(f"You hit!")
    attack = random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll <= 10:
    if roll == 1:
        print(f"You rolled a critacal failure! The monster gets a free attack!")
        damage = random.randint(1,10) + 2
        player_hp -= damage
        print(f"You took {damage} you now have {player_hp} HP.")
    else:
        print(f"You missed!")
else:
    print(f"That shouldn't be possible")

print("your turn is over.")