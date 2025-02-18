import random


#player initial stats
hp = 50
money = 10

def roomg():
    ids_array = ["1","2","3","4"]
    ids_array2 = ["Gold","SwapperL","Mud","Cure","Plus"]
    hp_range = [1,2,3,4,5]

    room = [[''] * 3 for _ in range(5)]
    #setting the hp ammount in monster cards
    for i in range(len(room)):
        room[i][0] = ids_array[random.randrange(4)]
        room[i][1] = ids_array2[random.randrange(5)]
        for e in range(3):
            if room[i][e] == ids_array[0] :
                room[i][2] = hp_range[4]

    
    return room



room = roomg()
print(room)
