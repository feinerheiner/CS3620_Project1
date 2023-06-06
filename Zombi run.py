
class Player:
    __weapon = 0
    __key = 0

    def __init__(self, name):
        self.name = name

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_key(self, key):
        self.__key = key

    def get_weapon(self):
        return self.__weapon

    def get_key(self):
        return self.__key

story = [
    # 0
    "Welcome to Zombie Run. The point of the game is to make it out of the building. You will be faced with"
    "\nquestions. Your choices will impact the outcome of the game. \nChoose wisely.\n\n"
    "You find yourself in an empty room with 3 doors one to the left, right, and directly in front of you.",
    # 1
    "You walk through the door into an empty hallway with flickering lights."
    "\nYou see that there are many doors in the hallway, and you can hear screams coming from"
    "\nsomewhere else in the building.",
    # 2
    "You open the door to a bathroom. You hear a wet dripping sound. A Zombie jumps out of the stall"
    "\nand bites your neck.",
    # 3
    "You open the door to a boiler room. As you look around you see a pipe wrench on the floor."
    "\nYour scared to take it because you dont want to make noise, but it could be good to fight"
    "\n with.",
    # 4
    "You see a door at the other end of the room.",
    # 5
    "You find one door that is open. It looks like an empty office, but as you look down your eyes find"
    "\na pool of blood and a lifeless body.",
    # 6
    "You see stairs that lead down to the main floor. You are nervous because the screaming is"
    "\ngetting louder.",
    # 7
    "You try to sneak around but another zombie walks out of a different room. It sees you and you"
    "\nwish you had a weapon. The zombie eats your brain.",
    # 8
    "Once at the stairs you see a person running away from a zombie. They both "
    "\nrun out of your view.",
    # 9
    "You run down the stairs yelling your beast war cry. When you get down the stairs, you see the"
    "\nzombie running towards you. You wield the pipe wrench like it was excalibur and bash the "
    "\nzombie in the head.",
    # 10
    "You try to sneak around, not caring about the other person. You can hear the zombie feeding on"
    "\nits kill.",
    # 11
    "In their hands is a key. Written on the key chain is 'Secret exit'.",
    # 12
    "You walk past the body not daring to touch it.",
    # 13
    "There is nothing else in the room. you decide to exit the room and continue down the hallway.",
    # 14
    "The person you saved comes out of a broom closet that they where hiding in. They ask to join"
    "\nyou.",
    # 15
    "You walk up behind it and kill the zombie, but it is too late for the person that it was"
    "\nfeeding on. Next to the body you see what seems to be a map.",
    # 16
    "you sneak past without it detecting you. you find a room to hide in. In the room you see a key"
    "\nhole in the wall.",
    # 17
    "You let them join you, after all there is strength in numbers. You share your findings with"
    "\neach other.",
    # 18
    "You tell them to find their own way. You dont trust others anymore.",
    # 19
    "You look at the blood stained mad and see that the other person has marked rooms and what they"
    "\nfound in them. There is a room marked with a keyhole.",
    # 20
    "You exit the room to wonder down the hall and try to find a way out. You see what seems to be"
    "\nthe front door but there are too many zombies. You try to back up slowly but you step on some "
    "\nshattered glass. The horde of zombies see you.",
    # 21
    "You dont realize that the other person has been bitten. As you are searching the building for a"
    "\nway out, they turn into a zombie and feast on your flesh.",
    # 22
    "The other person tells you about a room with a keyhole in it.",
    # 23
    "You did not escape. \nThe End",
    # 24
    "Part of the wall opens to a secret hall that leads you out of the building to safety."
    "\nCongratulations!! You escaped! \nThe End"
]

choice = [
    # 0
    "...",
    # 1
    "\nChoose which door to go through.(Left/Front/Right)\n",
    # 2
    "\nTake wrench?(Yes/No)\n",
    # 3
    "\nCheck doors or continue down hallway?(Check/Continue)\n",
    # 4
    "\nUse your weapon and attack the zombie, or sneak around?(Attack/Sneak)\n",
    # 5
    "\nWould you like to search the body?(Yes/No)\n",
    # 6
    "\nWould you like to kill the zombie while its feeding or sneak past it?(Kill/Sneak)\n",
    # 7
    "\nDo you want them to join you?(Yes/No)\n",
    # 8
    "\nWould you like to pick up the map?(Yes/No)\n",
    # 9
    "\nGo to room marked with the keyhole?(Yes/No)\n",
    # 10
    "\nTry to use the key in the wall?(Yes/No)\n"
]

choice_location = 1
story_location = 0
end = 0
loopnum = 1


def decision(c):
    user_in = input(choice[c]).lower().strip()
    global choice_location
    global story_location
    global end
    if c == 1 and user_in == "left":
        story_location = 1
        choice_location = 3
    elif c == 1 and user_in == "front":
        f.write(story[2])
        f.write(story[23])
        print(story[2])
        print(story[23])
        end = 1
    elif c == 1 and user_in == "right":
        story_location = 3
        choice_location = 2
    elif c == 2 and user_in == "no":
        f.write(story[4])
        print(story[4])
        story_location = 1
        choice_location = 3
        p1.set_weapon(p1,0)
    elif c == 2 and user_in == "yes":
        f.write(story[4])
        print(story[4])
        story_location = 1
        choice_location = 3
        p1.set_weapon(p1, 1)
    elif c == 3 and user_in == "check":
        story_location = 5
        choice_location = 5
    elif c == 3 and user_in == "continue":
        f.write(story[6])
        print(story[6])
        story_location = 8
        if p1.get_weapon(p1):
            choice_location = 4
        else:
            f.write(story[8])
            f.write(story[7])
            f.write(story[23])
            print(story[8])
            print(story[7])
            print(story[23])
            end = 1
    elif c == 4 and user_in == "attack":
        f.write(story[9])
        print(story[9])
        story_location = 14
        choice_location = 7
    elif c == 4 and user_in == "sneak":
        story_location = 10
        choice_location = 6
    elif c == 5 and user_in == "yes":
        p1.set_key(p1, 1)
        f.write(story[11])
        f.write(story[13])
        print(story[11])
        print(story[13])
        story_location = 8
        if p1.get_weapon(p1):
            choice_location = 4
        else:
            f.write(story[8])
            f.write(story[7])
            f.write(story[23])
            print(story[8])
            print(story[7])
            print(story[23])
            end = 1
    elif c == 5 and user_in == "no":
        f.write(story[12])
        f.write(story[13])
        print(story[12])
        print(story[13])
        story_location = 8
        if p1.get_weapon(p1):
            choice_location = 4
        else:
            f.write(story[8])
            f.write(story[7])
            f.write(story[23])
            print(story[8])
            print(story[7])
            print(story[23])
            end = 1
    elif c == 6 and user_in == "kill":
        story_location = 15
        choice_location = 8
    elif c == 6 and user_in == "sneak":
        if p1.get_key(p1):
            story_location = 16
            choice_location = 10
        else:
            f.write(story[16])
            f.write(story[20])
            f.write(story[23])
            print(story[16])
            print(story[20])
            print(story[23])
            end = 1
    elif c == 7 and user_in == "yes":
        f.write(story[17])
        print(story[17])
        if p1.get_key(p1):
            story_location = 22
            choice_location = 9
        else:
            f.write(story[21])
            f.write(story[23])
            print(story[21])
            print(story[23])
            end = 1
    elif c == 7 and user_in == "no":
        f.write(story[18])
        f.write(story[20])
        f.write(story[23])
        print(story[18])
        print(story[20])
        print(story[23])
        end = 1
    elif c == 8 and user_in == "yes":
        story_location = 19
        choice_location = 9
    elif c == 8 and user_in == "no":
        f.write(story[20])
        f.write(story[23])
        print(story[20])
        print(story[23])
        end = 1
    elif c == 9 and user_in == "yes":
        if p1.get_key(p1):
            story_location = 16
            choice_location = 10
        else:
            f.write(story[16])
            f.write(story[20])
            f.write(story[23])
            print(story[16])
            print(story[20])
            print(story[23])
            end = 1
    elif c == 9 and user_in == "no":
        f.write(story[20])
        f.write(story[23])
        print(story[20])
        print(story[23])
        end = 1
    elif c == 10 and user_in == "yes":
        f.write(story[24])
        print(story[24])
        end = 1
    elif c == 10 and user_in == "no":
        f.write(story[20])
        f.write(story[23])
        print(story[20])
        print(story[23])
        end = 1
    else:
        print("Incorrect value. Please try again")
        decision(c)


def narrative(s):
    f.write(story[s])
    print(story[s])
    f.write(choice[choice_location])
    decision(choice_location)


p1 = Player
f = open("gamePlay.txt", "w")
f.close()
f = open("gamePlay.txt", "a")

while not end:
    narrative(story_location)
    print(loopnum)
    loopnum += 1

print("Your game has been printed out on 'gamePlay.txt'. \nThanks for playing")
f.close()

