import random

print('I am thinking of a number between 1 and 20')
print('Take a guess')

number = random.randint(1,20)

i = 0
while True:
    i = i + 1
    guess = int(input())       
        
    if guess == number :
        break
    elif guess > number :
        print('My number is lower')
    else :
        print('My number is higher')

print('Good Job, sir! You guessed my number in ' + str(i) + ' tries')
        
    
