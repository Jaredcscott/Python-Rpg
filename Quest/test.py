from Quest_funcs import *

jared = Player(10,1,1,1,1,"Jared")

weapons_list = initialize_weapons_list()
jared.equip(5,weapons_list[1])

print(jared.equipped[5])
