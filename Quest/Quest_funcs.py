import random
import time


class Weapon:
    def __init__(self, damage, name):
        self.dmg = damage
        self.name = name


class Player:
    def __init__(self, health, attack, defense, magic, level, name):
        self.hp = health
        self.atk = attack
        self.defn = defense
        self.mag = magic
        self.lvl = level
        self.nm = name
        self.equipped = [0,0,0,0,0,0,0]

    def equip(self,num,item):
        '''
        [0] = head
        [1] = body
        [2] = legs
        [3] = feet
        [4] = arms
        [5] = right hand
        [6] = left hand
        '''
        self.equipped[num] = item.name




    def lose_health(self, damage):
        self.hp = self.hp - damage

    def gain_health(self, health_gain):
        self.hp = self.hp + health_gain

    def gain_level(self):
        self.hp = self.hp + 2
        self.atk = self.atk + 1
        self.defn = self.defn + 1
        self.mag = self.mag + 1
        self.lvl = self.lvl + 1

    #def attack():

class Monster:
    def __init__(self, health, attack, defense, magic, level, name):
        self.hp = health
        self.atk = attack
        self.defn = defense
        self.mag = magic
        self.lvl = level
        self.nm = name

    def lose_health(self, damage):
        self.hp = self.hp - damage

    def gain_health(self, health_gain):
        self.hp = self.hp + health_gain

def initialize_monster_list(player):

    monster_list = []

    orc = monster(15,3,3,0,random.randint(1,player.lvl),"Orc")
    wolf = monster(20,3,5,0,random.randint(1,player.lvl),"Wolf")
    rat = monster(10,2,2,0,random.randint(1,player.lvl),"Rat")

    monster_list.append(orc)
    monster_list.append(wolf)
    monster_list.append(rat)
    return monster_list

def fight(player,monster):
    print("you are about to battle a %s"%str(monster.nm))
    #battle
    while monster.hp > 0 and player.hp > 0:
        player_roll = random.randint(1, 40 - player.atk)
        monster_roll = random.randint(1,50 - monster.atk)

        if player_roll % 4 != 0:
            print("You missed!")
        elif player_roll % 4 == 0:
            print("Hit!!")
            monster.lose_health(player.atk)

        if monster_roll % 4 != 0:
            print("The monster missed!")
        elif monster_roll % 4 == 0:
            print("You have been hit!!    :(")
            print("%s health lost!"%str(monster.atk - player.defn))
            player.lose_health(monster.atk - player.defn)

    if monster.hp <= 0 and player.hp >= 0:
        print("Battle is over!, You have won!! :)")
    if monster.hp >= 0 and player.hp <= 0:
        print("Battle is over!, You have lost!! :(")




def initialize_weapons_list():
    sword = Weapon(2,"Sword")
    spear = Weapon(3,"Spear")
    axe = Weapon(4,"Axe")

    weapons_list = []
    weapons_list.append(sword)
    weapons_list.append(spear)
    weapons_list.append(axe)

    return weapons_list
