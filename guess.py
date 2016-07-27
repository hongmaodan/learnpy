from random import randint

def numcheck(numin):
    if numin >= '0' and numin <= '9':
    	return int(numin)
    else:
        return -1

target = randint(0,99)

guessnu = -1
guessct = 0

while guessnu != target:
    guessraw = raw_input("Input your guessing number, Only number < 100!: ")
    print("Your guessing is %s"%guessraw)
    guessnu = numcheck(guessraw)
    while (guessnu > 99) or (guessnu < 0):
        guessraw = raw_input("Input your guessing number, Only number < 100!: ")
	print("Your guessing is %s"%guessraw)
        guessnu = numcheck(guessraw)
    guessct+=1
    if guessnu < target:
        print("Too small")
    elif guessnu > target:
        print("Too big")
    else:
        print("Bingo!")
        print("You guessed %d times"%guessct)
