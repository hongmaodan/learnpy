from random import randint
target=randint(1,100)
guessct=1

print('Guess what I think?')
bingo=False

while bingo==False:
    answer=input()

    if answer<target:
        print('too small!')
        guessct+=1

    if answer>target:
        print('too big!')
        guessct+=1

    if answer==target:
        print('BINGO!')
        bingo=True
        print('You guessed %d times'%guessct)
