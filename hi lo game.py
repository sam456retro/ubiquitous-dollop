import random
answer = random.uniform(1,10)
answer = round(answer)
all_guess = []
k = 0
while True:
    while True:
        try:
            guess = int(input('enter your guess:  '))
            if guess > 10:
                print('only numbers less than 10 allowed !!')
            else:
                break
        except:
            print('only numbers please!!')

    if guess > answer + 3:
        if guess in all_guess:
            print('you have already guesed that number !!')
            k += 1
        else:
            print('your guess is too high !!')
            all_guess.append(guess)
            k += 1
    
    elif guess <= (answer + 2) and guess > answer:
        if guess in all_guess:
            print('you have already guesed that number !!')
            k += 1
        else:
            print('your guess is close !!')
            all_guess.append(guess)
            k += 1
   
    elif guess == answer:
        k += 1
        print('congratulations ! You guessed the number in {} attempts !'.format(k))
        break
    
    elif guess < answer and guess >= (answer - 2):
        if guess in all_guess:
            print('you have already guesed that number !!')
            k += 1
        else:
            k += 1
            print('your guess is close !!')
            all_guess.append(guess)
    else:
        if guess in all_guess:
            k += 1
            print('you have already guesed that number !!')
        else:
            k += 1
            print('your guess is too low !!')
            all_guess.append(guess)
