import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    lives=4
    while feedback != 'c' and lives>0:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        lives-=1
        print("Computer have",lives," lives left")
        if(lives==0):
            print("Computer lost!")
            break
        if(feedback=='c'):
            print(f'Yay! The computer guessed your number, {guess}, correctly!')
computer_guess(10)