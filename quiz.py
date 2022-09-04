quiz = {
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



def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case-sensitive.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
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
intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
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
        break
