import random

def play():
    user = input("Play? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'TIE'

    if is_win(user, computer):
        return 'YOU WON!'

    return 'YOU LOST!'

def is_win(player, opponent):
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
