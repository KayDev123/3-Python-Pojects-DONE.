import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x} (guess) $ '))
        except TypeError:
            print('Only numbers!!')
        
        if guess > random_number:
            print('Sorry, The Guess is high!!')
        
        if guess < random_number:
            print('Sorry,  to low!!')

    print(f'Yay, the number was {random_number}. You guessed right! Correctly!!')
    
#---------------------------------------------------------------------------------------------------------

def computer_guess(x):
    low =  1
    high = x
    feedback = ''

    while feedback != 'c' and low !=  high:
        if low != high:
            Guess = random.randint(low, high)
        else:
            Guess = high or low

        feedback = input(f'Hey,  Is  {Guess} okay? Or too high (H)? Or low (L)? or Correct! (C) > ').lower()

        if feedback == 'h':
            high = Guess - 1
        elif feedback == 'l':
            low = Guess + 1
    
    print(f'Yay, the number was {Guess}. You guessed it right computer! Correctly!!')



computer_guess(10)
        




guess(10)
