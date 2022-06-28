from sys import exit

# Item Status
have_bone = False
have_key = False
have_sword = False
file_name = "book.txt"
items = ["bone", "sword", "gold key", "book"]
name = ""


def player_name():
    print("\nHello, enter your name to begin the game: ")
    global name
    name = input("> ")
    print(f"Hello, {name} welcome to the adventure: ")


def dead(why):
    print(why, "good job!")
    exit(0)


def show_items():
    print("\nNow we have these stuff: ")
    for i in items:
        print(i)


def read_book():
    hint = open(file_name, "r")
    print(hint.read())
    hint.close()


def boss():
    boss_move = False
    print("\nThe boss is badass, what do you do?")
    while True:
        choice = input("> ")
        if not boss_move and "throw coin" in choice:
            boss_move = True
        elif boss_move and "throw coin" in choice:
            dead("\nBoss slay your head")
        elif boss_move and "throw sword" in choice:
            print("\nYou win. Congratulation!")
            exit(0)


def treasure_room():
    print("\nYou are now in an treasure room")
    print("There are plenty of treasure here")
    print("You plan to take some of them, how much do you take?")
    how_much = input("> ")
    try:
        how_much = int(how_much)
    except ValueError:
        print("\nMan learn to type a number")
        treasure_room()
    if how_much < 50:
        print("\nNice, you're not greedy, the boss show up now")
        boss()
    else:
        dead("\nYou are greedy bastard!")


def library_room():
    print("\nThere are a plenty of things on the ground")
    print(f"What do you do now, {name}?")
    choice = input("> ")
    if "see" in choice:
        show_items()
        library_room()
    elif "read book" in choice:
        print("\nIt reveal something")
        read_book()
        library_room()
    elif "take all" in choice:
        global have_bone, have_key, have_sword
        have_bone = True
        have_key = True
        have_sword = True
        print("\nNice choice, now we have all thing we need to go to the wolf room")
        wolf_room()
    else:
        print("\nI have no idea what you are trying to mention here")
        library_room()
# print("You have fall, everything become dark.")
# wolf_room()


def gold_room():
    print("\nYou are in front of a room with golden door")
    print("Door is locked, what do you do?")
    choice = input("> ")
    if "gold key" in choice and have_key is True:
        treasure_room()
    elif "gold key" in choice and have_key is False:
        print("\nYou don't have any key")
        gold_room()
    elif "return" in choice:
        library_room()
    else:
        print("\nI have no idea what are you talking about?")
        gold_room()


def wolf_room():
    print("\nA giant wolf is stand in front of you. What do you do?")
    choice = input("> ")
    if "throw bone" in choice and have_bone is True:
        gold_room()
    elif "throw bone" in choice and have_bone is False:
        dead("\nYou have nothing to throw, the wolf just eat your face off")
    else:
        print(f"Try something smarter {name}.")
        wolf_room()


def main():
    player_name()
    print("You are in a dark room {}, let chose where to begin".format(name))
    print("""
    There are a room on the right and a door on the left
    Which one do you take?
    """)
    choice = input("> ")
    if "left" in choice:
        wolf_room()
    elif "right" in choice:
        library_room()
    else:
        dead("\nYou stumble around the room until you starve.")


if __name__ == "__main__":
    main()
