def quiz_master():
    """
    Encountering the quiz_master, the player chooses to attack, answer or leave.
    - attack: player dies, and it is game over.
    - answer: answer the questions and hopefully continue the quest.
    - leave: player turns around and goes the way he came.
    """
    # Actions on the guard
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
            elif action == "attack":
                you_died(
                    "The man was lightening quick!"
                    "His razer sharp teeth were in your neck before you could blink."
                    "You feel the life seeping from your body. \n<GAME OVER>")

    def quiz_room():
        """
        The player finds a room.
        An wrinkly old man asks some riddles.

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

        )