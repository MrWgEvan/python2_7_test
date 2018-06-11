number = 25
running = True

while running:
    guess = int(input("enter an Integer:  "))
    if guess == number:
        print ('you guessed it. ')
        running = False
    elif guess < number:
        print ('a little lower. ')
    else:
        print ('a little higher.')
else:
    print ('the game is over.')
