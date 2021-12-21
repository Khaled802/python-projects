import random
from os import system
from black_jack_logo import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def get_random():
    rand_index = random.randrange(0, len(cards))
    return cards[rand_index]

def state(computer, player):
    print(f'\tYour cards are {player}, current score: {sum(player)}')
    print(f'\tcomputer\'s first card: {computer[0]}')
    choice = input('Type \'yes\' if you want anthor card, otherwise \'no\': ').strip().lower()
    return ('yes' in choice)

def correctenss(computer, player):
    while sum(player) > 21 and 11 in player:
        player[player.index(11)] = 1

    if sum(computer) < 17:
        computer.append(get_random())
    

def result(computer, player):
    computer_score = sum(computer)
    player_score = sum(player)
    print(f"Your score: {player_score}, cards {player}")
    print(f'Computer score: {computer_score}, cards {computer}')
    if player_score > 21:
        print("Game Over")
        return
    if computer_score > 21:
        print("Winning╰(*°▽°*)╯")
        return

    if player_score > computer_score:
        print("Winning╰(*°▽°*)╯")
    elif player_score < computer_score:
        print("Game Over")
    else:
        print("Draw!!!")
    

def play():
    computer = []
    computer.append(get_random())
    computer.append(get_random())

    player = []
    player.append(get_random())
    player.append(get_random())

    choice = state(computer, player)

    if choice:
         player.append(get_random())

    correctenss(computer, player)
    result(computer, player)

while True:
    print(logo)
    play()
    want_continue = input('Type \'yes\' if want to play again, otherwise type \'no\': ').strip().lower()
    if 'yes' not in want_continue:
        break
    system('cls')
