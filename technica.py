def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 2:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 1:
                guess = input("try again")
            attempt = attempt + 1
    if attempt == 2:
        print("The Correct answer is ",answer)


score = 0
print("Guess the Fruit")
guess1 = input("What fruit is green?")
check_guess(guess1, "lime")
guess2 = input("What food is technically a fruit? ")
check_guess(guess2, "tomato")
guess3 = input("What fruit is sour? ")
check_guess(guess3, "lemon")
print("Your Score is "+ str(score), ",good job!")