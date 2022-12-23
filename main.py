# Rock Paper Scissors
import random
answers = ('Rock', 'Paper', 'Scissors')

user_score = 0
program_score = 0


def compare(a, b):
    global user_score
    global program_score

    if a == b:
        print(a, "vs", b, ">>>> Equality")
    elif a == 'Rock' and b == 'Paper':
        print(a, "vs", b, ">>>> You win !")
        user_score += 1
    elif a == 'Paper' and b == 'Rock':
        print(a, "vs", b, ">>>> Program wins !")
        program_score += 1
    elif a == 'Paper' and b == 'Scissors':
        print(a, "vs", b, ">>>> You win !")
        user_score += 1
    elif a == 'Scissors' and b == 'Paper':
        print(a, "vs", b, ">>>> Program wins !")
        program_score += 1
    elif a == 'Scissors' and b == 'Rock':
        print(a, "vs", b, ">>>> You win !")
        user_score += 1
    elif a == 'Rock' and b == 'Scissors':
        print(a, "vs", b, ">>>> Program wins !")
        program_score += 1
    else:
        print('Only "Rock" "Paper" and "Scissors" are available')


def play_again():
    answer = input("""Do you want to play again? -> Y / N
>>>> """)

    if answer.lower() == 'y' or answer.lower() == 'yes' or answer.lower() == '':
        play_game()
    elif answer.lower() == 'n' or answer.lower() == 'no':
        print("Your score ->", user_score, "\nPrograms score ->", program_score)
        exit(0)


def play_game():
    rand = random.choice(answers)
    users_a = input("""Choose between Rock Paper and Scissors
>>>> """)

    compare(rand, users_a.capitalize())
    play_again()


play_game()
