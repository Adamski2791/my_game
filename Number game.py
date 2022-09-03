secret_number = 6

print(
    """
    +=======================================+
    | Welcome to my game, adventurer!       |
    | I hope you have been paying attention.|
    | I have a guessing game for you.       |
    | The only way out of the room is       |
    | to answer the question correctly.     |
    | How many items were in the chest?     | 
    | So, what is the secret number?        |
    +=======================================+
    """)

user_number = int(input("Enter the number: "))

while user_number != secret_number:
    print("Ha ha! You're stuck in my room!")
    user_number = int(input("Enter the number again: "))
print(secret_number, "Well done, ! You adventurer are free now.")
