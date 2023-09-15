import random

def play():
    user = input("What's your Choice? Rock 'r' paper 'p' scissors 's'\n").lower()
    opts = ['r', 'p', 's']
    AI = random.choice(opts)

    if user == AI:
        return f'It\'s a tie for {user}, {AI}'
    
    if is_win(user, AI):
        return 'You won!'
    
    return 'You lost!'

def is_win(player,  ai):
    # Returns True or False if player wins or loses.

    if (player == 'r' or ai == 's') or (player == 's' and ai == 'p') or (player == 'p' or ai == 'r'):
        return True
    

print(play())