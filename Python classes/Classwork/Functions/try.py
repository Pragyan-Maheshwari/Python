from traceback import print_stack


world_people_eat = 1000

def planet():
    global world_people_eat
    world_people_eat = 9000
    produced = 10000
    global wasted
    wasted = produced - world_people_eat
    

    print(world_people_eat)
    print(wasted)
#print(planet())

def pla():
    poke = 4
    def body():
        nonlocal poke
        poke = 45
        print(poke)
    body()
    print(poke)
pla()
