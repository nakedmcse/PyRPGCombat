# RPG Combat illustrating passing functions
import random

# Player
class Player:
    def __init__(self,name,skill,stamina,weapon,armor):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.weapon = weapon
        self.armor = armor
        print(f"Created player {self.name} with skill {self.skill} and stamina {self.stamina}")

    def isDead(self):
        return self.stamina <= 0
    
    def hitOpponent(self):
        return random.randint(1,12) <= self.skill
    
    def takeHit(self,weapon):
        damage = self.armor(weapon)
        if damage < 0:
            self.stamina = self.stamina + damage
            print(f"Player {self.name} took {0-damage} damage")

# Weapons
class Weapons:
    def dagger():
        return random.randint(1,4)

    def sword():
        return random.randint(1,8)
    
    def club():
        return random.randint(1,6)
    
    def greatsword():
        return random.randint(1,10)
    
# Armor
class Armors:
    def none(func):
        return 0-func()
    
    def padded(func):
        return random.randint(1,6) - func()
    
    def chain(func):
        return random.randint(1,8) - func()
    
# Main Loop
playerA = Player("A",random.randint(1,12),random.randint(1,12),Weapons.sword,Armors.chain)
playerB = Player("B",random.randint(1,12),random.randint(1,12),Weapons.club,Armors.padded)

done = False
while done==False:
    if playerA.hitOpponent():
        playerB.takeHit(playerA.weapon)

    if playerB.hitOpponent():
        playerA.takeHit(playerB.weapon)

    if playerA.isDead():
        print(f"Player {playerA.name} was slain")
        done = True

    if playerB.isDead():
        print(f"Player {playerB.name} was slain")
        done = True