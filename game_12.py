#
# Added coded in main(),and create a function to ask for your name and return it.
#

# Global variables#
backpack = []
diamonds = False
gold = False
crown = False
sword = False
cork = False
chalice = False


# ACTIONS #
def you_died(why):
    """
    In: Passing in the string showing player how they dies

    Result:
    Prints reason why they player died.
    Programme exits without error.
    """
    print("{}. Good job!".format(why))

    # This exits the program entirely.
    exit(0)


def sail_home():
    """
    This is where you get your happy ending
    """
    print("The cork fits the hole perfectly and you stop the leak.")
    if chalice:
        print("You bail the excess water with the chalice and head across the lake, to freedom.")
        print("You leave with your riches and live to fight another day! Well done!")
        exit(0)


# END ACTIONS #

# CHARACTERS #


def guard():
    """
    Encountering the guard, the player chooses to attack, check or sneak.
    - attack: player dies, and it is game over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    """
    # Actions on the guard
    actions_dict = {
        "check": "You see the guard is still sleeping, you need to get to that door on the right of him. What are you "
                 "waiting for?",
        "sneak": "You approach the guard, he's still sleeping. Reaching for the door, you open it slowly and slip out.",
        "attack": "You swiftly run towards the sleeping guard and knock him out with the hilt of your shiny sword. "
                  "Unfortunately it wasn't hard enough."}

    # While loop
    while True:
        action = input("What do you do? [attack | check | sneak] >").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("You just slipped through the door before the guard realised it.")
                print("You have entered a new room.\n")
                quiz_room()
            elif action == "attack":
                you_died(
                    "Guard woke with a grunt, and reached for his dagger and before you know it, the world goes dark "
                    "and you just died. \n<GAME OVER>")


def dragon():
    """
    Encountering the dragon, the player chooses to attack, talk or sneak.
    - attack: player dies, and it is game over
    - talk: asks the dragon a question
    - sneak: player sneaks past the dragon and finds a passage
    """
    # Actions on the dragon
    dragon_actions_dict = {
        "talk": "You ask the dragon for directions. What's the worst that could happen?",
        "creep": "You approach the dragon on tip toes, he's watching but can't see you."
                 "Reaching for the door, you open it slowly and slip out.",
        "attack": "You swiftly run towards the dragon waving your shiny sword. A blast of fire consumes you. "
                  "You are now a crispy critter."}

    # While loop
    while True:
        action = input("What do you do? [attack | creep | talk] >").lower()
        if action in dragon_actions_dict.keys():
            print(dragon_actions_dict[action])
            if action == "creep":
                print("You just slipped through the door before the dragon realised it.")
                print("You are now outside the dragons lair.\n")
                return
            elif action == "attack":
                you_died(
                    "The dragon was too fast and you got flamed grilled like a whopper "
                    "and you died. \n<GAME OVER>")


def queen():
    """
    Encountering the queen, the player chooses to attack, check or sneak.
    - attack: player dies, and it is game over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    """
    # Actions on the guard
    queen_actions_dict = {
        "talk": "You clear your throat and the queen turns around. She is beautiful. .",
        "sneak": "You turn away quietly. Reaching for the door and slip out.",
        "attack": "You swiftly run towards the queen and aim a blow with your shiny sword. "
                  "You don't see the guard, and he cuts you down, as you enter the room."}

    # While loop
    while True:
        action = input("What do you do? [attack | talk | sneak] >").lower()
        if action in queen_actions_dict.keys():
            print(queen_actions_dict[action])
            if action == "sneak":
                print("You just slipped through the door before the queen realised it.")
                print("You are now outside, home free! Huzzah!\n")
                return
            elif action == "talk":
                print("You are so taken with her beauty, you don't see the guard beside the door")
                you_died(
                    "The guard was faster that anyone you had ever seen before and his blade was true!"
                    "Your head was separated from your shoulders and you died. \n<GAME OVER>")
            elif action == "attack":
                you_died(
                    "The guard was faster that anyone you had ever seen before and his blade was true!"
                    "Your head was separated from your shoulders and you died. \n<GAME OVER>")


def quiz_master():
    """
    Encountering the quiz_master, the player chooses to attack, answer or leave.
    - attack: player dies, and it is game over.
    - answer: answer the questions and hopefully continue the quest.
    - leave: player turns around and goes the way he came.
    """
    quiz_master_actions_dict = {
        "attack": "You swing your sword, like a flash. It's slices through the air and then into the ragged man."
                  "The old man is faster still and he sinks his sharp teeth into your neck."
                  "He severs an artery and you bleed out quickly,as he drinks your blood!",
        "answer": "You decide to take the old man's quiz.",
        "leave": "You turn away. Reach for the door and head back the way you came, feeling like a coward.",
    }
    # While loop
    while True:
        action = input("What do you do? [attack | answer | leave] >").lower()
        if action in quiz_master_actions_dict.keys():
            print(quiz_master_actions_dict[action])
            if action == "leave":
                print("You turn tail. There is something evil in this room and your skin crawls.")
                print("You can't leave quick enough, and you feel that you have saved your skin. \n")
                return
            elif action == "answer":
                print("You are wary of the man, but you are smart and like a gamble.")
                print("You say, 'Ask your questions demon. You do not scare me!")
                quiz()
            elif action == "attack":
                print(you_died(
                    "The man was lightening quick!"
                    "His razor sharp teeth were in your neck before you could blink."
                    "You feel the life seeping from your body. \n<GAME OVER."))



# END CHARACTERS #


# ROOMS #
def blue_door_room():
    """
    The player finds a treasure chest, options to investigate the treasure chest or guard.

    If player chooses
    - Treasure chest: show its contents; option to take treasure or ignore it (proceeds to guard)
    - Guard: After checking treasure chest, ignoring treasure chest to check guard, it calls guard() function
    """
    # So, our treasure_chest list contains 6 items.
    treasure_chest = ["diamonds", "gold", "crown", "sword", "cork", "chalice"]
    print(
        "You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the "
        "door")

    # Ask player what to do.
    action = input("What do you do? Left or right? > ")

    # This is a way to see if the text typed by the player is in the list
    if action.lower() in ["treasure", "chest", "left", "l"]:
        print("Ooh, treasure!")
        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)

            # So much treasure, what to do? Take it or leave it.
            print("What do you want to do?")
            # Get number of items in treasure chest with len))
            num_items_in_chest = len(treasure_chest)

            print(f"Take all {num_items_in_chest} treasure, press '1'")
            print("Leave it, press '2'")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                treasure_chest.remove("sword")
                backpack.append("sword")
                print("\t Your crappy sword is dull and rusty. You decide that it would be wise to take the new one.")
                print("\t You take the shinier sword from the treasure chest. It does look exceedingly shiny.")
                print("\t Woohoo! Bounty and a shiny new sword. /drops your crappy sword in the empty treasure chest.")
                print("\t You try to take all the loot, but it won't fit.")
                print("\t Your backpack is pretty small, and you can only fit 3 more items.")
                print("\t Which items should you take?")
                print(f"There is still {treasure_chest} in the chest.")
                treasure_chest.append("crappy sword")
                while len(backpack) <= 4:
                    item = input("Enter item : ")
                    treasure_chest.remove(item)
                    backpack.append(item)
                    print(f"You have placed {item} in your backpack")
                    print(f"There is still {treasure_chest} in the chest.")
                    print(f"You have {backpack} in your backpack")
                    if len(backpack) == 4:
                        print("Do you want to check the guard, go back the way you came or move on?")
                        action = input("What do you do? Check guard, move back or move on? > ")
                        if action.lower() in ["check guard", "guard", "g"]:
                            guard()
                        elif action.lower() in ["move back", "back", "b"]:
                            start_adventure()
                        elif action.lower() in ["move on", "on", "forward"]:
                            quiz_room()


            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
        elif choice == "2":
            print("Who needs treasure, let's get out of here.'")
    elif action.lower() in ["guard", "right","r"]:
        print("Let's have fun with the guard.")
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")
    guard()


def secret_corridor():
    """
    The player finds a secret corridor.

    If player chooses
    - Left is a lake. There is a boat. If they take the boat they can exit
    - Right, enters the Queens chamber.
    """

    print(
        "You run from the dragon and stumble into a secret corridor."
        "You walk down the creepy corridor. There are stalactites and a constant dripping of water "
        "A rat scurries past your feet, making you almost drop your sword."
        "You come to a T-junction, to the left is a lake and on the shore, is a small and battered looking wooden boat."
        "To the right, is a strong looking wooden door. It is slightly ajar and there is light coming from inside.")

    # Ask player what to do.
    action = input("What do you do? left or right > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["left", "lake", "boat"]:
        print("This might be a way out?")
        print("Get in the boat? Press '1'")
        print("Go back to the door? Press '2'")
    if action.lower() in ["right", "door", "r"]:
        print("Feeling a bit nosey?")
        print("Let's go in!")
        queens_chamber()

    choice = input("1 for boat or 2 for door> ")
    if choice == "1":
        print("You climb inside the boat.")
        print("You push the boat from the shore.")
        print("You notice a leak. You feet are getting wet.")
        if cork:
            sail_home()
    else:
        you_died("You are too far from the shore and you can't swim! You drown!")

        if choice == "2":
            print("The door swings open with a creak.")
            print("You look inside and the room looks like a sleeping chamber.")
            print("It is very plush, with ornate carvings and paintings on the wall.")
            print("A woman has her back to you and is brushing her hair, while looking in the mirror.")
            print("You notice her crown sitting on the table beside her. This must be the queen!")
            queen()


def red_door_room():
    """
    The red door room contains a red dragon.

    If a player types "flee" as an answer, player returns to the room with two doors,
    otherwise the player dies.
    """
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        secret_corridor()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")


def queens_chamber():
    print("You look inside and the room looks like a sleeping chamber.")
    print("It is very plush, with ornate carvings and paintings on the wall.")
    print("A woman has her back to you and is brushing her hair, while looking in the mirror.")
    print("You notice her crown sitting on the table beside her. This must be the queen!")
    queen()


def quiz_room():
    """
    The player finds a room.
    A wrinkly old man asks some riddles.

    If player chooses
    - To leave and go
    Or answer questions to pass through and gain a prize.
    """

    print(
        "You enter a room. At first you think it's empty. There are a pile of rags in a heap on the ground."
        "A strange noise like a banshees wail and wind starts swirling. "
        "The rags get caught in the wind and start to rise."
        "The wind begins to ebb and you are standing face to face, with the oldest man that you have ever seen."
        "He looks through you and his eyes start to burn like embers."
        "The wind and the wailing subside and the man addresses you with a deep and rasping voice"
        "If you answer my riddles, you may leave with your hearts desires."

    )

    # Ask player what to do.
    action = input("What do you do? leave or stay > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["leave", "go", "back"]:
        print("You turn round?")
        print("Leave the way you came?")
        blue_door_room()
    if action.lower() in ["answer", "in", "stay"]:
        print("You can do this!")
        print("Let's go in!")
        quiz_master()

def quiz():

    riddles = {
        1:
            {"question": "What can bring back the dead; make you cry, make you laugh, make you young; is born in an "
                         "instant, yet lasts a "
                         "lifetime.", "answer": "Memory"},
        2: {
            "question": "This thing all things devour: birds, beasts, trees, flowers; gnaws iron, bites steel; grinds "
                        "hard stones to the "
                        "meal.", "answer": "Time"},
        3: {
            "question": "Some try to hide, some try to cheat; but time will show, we always will meet. Try as you might "
                        "to guess my name.",
            "answer":
                "Death"},
        4: {
            "question": "As small as your thumb, I am light in the air. You may hear me before you see me, but trust that "
                        "I'm here.",
            "answer":
                "Hummingbird"},
        5: {
            "question": "I'm alive, but without breath; I'm as cold in life as in death; I'm never thirsty, though I "
                        "always drink.",
            "answer": "Fish"}
    }



    def check_ans(quest, ans, att, total):
        """
        Takes the arguments, and confirms if the answer provided by user is correct.
        Converts all answers to lower case to make sure the quiz is not case-sensitive.
        """
        if riddles[quest]['answer'].lower() == ans.lower():
            print(f"Correct Answer! \nYour score is {total + 1}!")
            return True
        else:
            print(f"Wrong Answer :( \nYou have {att - 1} left! \nTry again...")
            return False


    #def print_dictionary():
        #for question_id, ques_answer in riddles.items():
            #for key in ques_answer:
                #print(key + ':', ques_answer[key])


    def quiz_intro_message():
        """
        Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
        Returns true regardless of any key pressed.
        """
        print("In my lair you'll answer me. \nThese 5 questions and you'll see?")
        print("Count your chances, 1 , 2, 3. ")
        print("If you fail, your blood feeds me.")
        input("Press Enter to start the trial! ")
        return True


    # python project.py
    intro_message()
    while True:
        score = 0
        for question in riddles:
            attempts = 3
            while attempts > 0:
                print(riddles[question]['question'])
                answer = input("Enter Answer : ")
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1
        if score < 5:
            print("You have failed your mission and now I will devour you!")
            print(" This is the last thing that you ever heard.")
            break
        else:
            print(f"Your final score is {score}!\n\n")
            print("You have bested me. Your wisdom is boundless. Pass in peace.")
            print("You must be on your way. Where will you go? Forward there is a door, or back the way you came?")



# END ROOMS #


def get_player_name():
    """
    Gets players name, may or may not be renamed depending on player's choice.
    Returns: Player name back (altered or unaltered)
    """
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    name = input("What's your name? > ")

    # This is just an alternative name that the game wants to call the player
    alt_name = "Rainbow Unicorn"
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print(f"You are fun, {name.upper()}! Let's begin our adventure!")

    elif answer.lower() in ["n", "no"]:
        print(f"Ok, picky. {name.upper()} it is. Let's get started on our adventure.")
    else:
        print("Trying to be funny? Well, you will now be called {alt_name.upper()} anyway.")
        name = alt_name

    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in
    # get_player_name() function.
    # This is why indentation is important, variables declared in this block only exists in that block
    return name


def start_adventure():
    """
    This function starts the adventure by allowing two options for
    players to choose from: red or blue door

    Chosen option will print out the door chosen.
    """
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ")

    # Pick a door, and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")


def main():
    """
    Gets the players name by calling get_player_name() before starting the adventure.
    """
    player_name = get_player_name()

    ####################################################################
    # ACTIVITIES
    #
    # Read some of the best practices when writing Python code
    #   http://legacy.python.org/dev/peps/pep-0008/
    # Main thing is if you are using tabs, make sure it's 4-spaces,
    # most editors will convert it (check preferences/settings).
    #
    # Modify the code
    # - add taunting the guard or talking
    # - sword fight with the guard, and keep track of health points (HP)
    # - puzzles like 1+2 during an encounter
    # - modify blue_door_room()'s if statement,
    #   so it takes into account player typing "right" or "guard"
    #   Hint: Add another elif before the else statement
    #
    # So many if statements, this can be made simpler and easier to
    # maintain by using Finite State Machine (FSM)
    # You can find info about it, but it will mainly be touching
    # object-orient programming, which is another lesson for another day.
    #
    #####################################################################

    start_adventure()

    print("\nThe end\n")
    print(f"Thanks for playing, {player_name.upper()}")


if __name__ == '__main__':
    main()
