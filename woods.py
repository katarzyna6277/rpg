import random


def pick_berries(bag):
    bag["food"] += 1
    return bag


def win_with_wolf(bag):
    bag["food"] += 2
    life_change = -12
    return bag, life_change


def lose_with_wolves(bag):
    bag["food"] += 0
    life_change = -60


def do_nothing(bag):
    bag["gold"] += 0
    life_change = 0
    return bag, life_change


def woods_adventure(bag):
    print("1. Pick the berries to get 1 food \n2. Fight with wolves to get more 2 foods. \n3. Go back to the city")
    phrase = int(input("Write 1 or 2: "))
    with open('woods.txt', 'r') as fopen:
        lines = fopen.readlines()
    if phrase == 1:
        for line in lines[0:2]:
            print(line)
        fight_or_run = int(input("Do you want to fight (1), run (2)"))
        if fight_or_run == 1:
            fight_result1 = random.choice(["win", "lose"])
            if fight_result1 == "win":
                for line in lines[3:5]:
                    print(line)
                return win_with_wolf(bag)
            elif fight_result1 == "lose":
                print(lines[9])
                return lose_with_wolves(bag)
        if fight_or_run == 2:
            print(lines[5])
        if fight_or_run == 3:
            do_nothing(bag)
        bag = pick_berries(bag)
        return bag, 0
    elif phrase == 2:
        print(lines[6])
        print(lines[7])
        hunt_or_run = int(input("Do you want to fight (1) or run (2)?"))
        if hunt_or_run == 1:
            fight_result = random.choice(["win", "lose"])
            if fight_result == "win":
                print(lines[8])
                return win_with_wolf(bag)
            elif fight_result == "lose":
                for line in lines[9:11]:
                    print(line)
                return lose_with_wolves(bag)
        if hunt_or_run == 2:
            print(lines[5])
    elif phrase == 3:
        print("ok")
        return do_nothing(bag)
    else:
        print("This is not what i expected! Choose 1 or 2")

    return bag, 0
