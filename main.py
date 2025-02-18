import random

#generate the room
def roomg():
    ids_array = ["Monster","Item","Effect","Secret"]
    ids_array2 = ["Gold","SwapperL","Mud","Cure","Plus"]
    hp_range = [1,2,3,4,5]

    room = [[''] * 3 for _ in range(5)]
    #setting the type and hp ammount in cards
    for i in range(len(room)):
        room[i][0] = random.choice(ids_array)
        room[i][1] = random.choice(ids_array2)
        room[i][2] = hp_range[0]


        for e in range(3):
            if room[i][e] == ids_array[0]:
                room[i][2] = hp_range[4]

    
    return room

#show the room in order
def sroom():
    for p in range(5):
        print(f' {p} {room[p]}')

def stroom():
    #add the value in here if the player hasve some items
    global hp
    for i in range(len(room)):
        print(f' {hp} "-" {room[i][2]}')
        hp = hp - room[i][2]
        print(hp)
    
    return hp
        

#main gameplay loop

#player initial stats
hp = 25
money = 10
swaps = 10
dmg = 10
#Generate the room and show to the player
room = roomg()
sroom()

#start game
#str = int(input("Type 1 to start:"))


stroom()

print(hp)



#if player dont have much more to do start this
if swaps <= 0:
    str = int(input("You dont have nothing to do more Type 1 Start:"))
    while str != 1:
        str = int(input("Invalid Type Again:"))

    
