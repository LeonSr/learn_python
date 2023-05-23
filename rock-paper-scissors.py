import random
while True:
    choices = ['rock','paper','scissors']

    computer = random.choice(choices)

    player = None
    while player not in choices:
        player = input('rock paper or scissors? :').lower()

    # tie

    if player == computer:
        print('player : '+player)
        print('computer : '+computer)
        print("tie")

    # player brings rock

    elif player == 'rock':
        if computer == 'paper':
            print('player : '+player)
            print('computer : '+computer)
            print("you lost")
        if computer == 'scissors':
            print('player : '+player)
            print('computer : '+computer)
            print("you won")

    # player bring scissors

    elif player == 'scissors':
        if computer == 'paper':
            print('player : '+player)
            print('computer : '+computer)
            print("you won")
        if computer == 'rock':
            print('player : '+player)
            print('computer : '+computer)
            print("you lost")

    #player brings paper

    elif player == 'paper':
        if computer == 'scissors':
            print('player : '+player)
            print('computer : '+computer)
            print("you lost")
        if computer == 'rock':
            print('player : '+player)
            print('computer : '+computer)
            print("you won")
    play_again = input('play again? (yes/no) :').lower()
    if play_again != "yes":
        break
print("bye!")