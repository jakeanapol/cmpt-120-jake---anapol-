def start():

    # target to guess
    answer = 'zebra'
    guess = ''
    guessNum = 1
    
    while(answer != guess and guessNum <= 3):

        guess = input('Guess an animal: ')

        if(answer == guess):
            print('good job')
            return True

        else:
            print('incorrect')    
            guessNum += 1

    return None

start()