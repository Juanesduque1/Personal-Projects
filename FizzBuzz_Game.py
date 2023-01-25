def game_fizzbuzz():
    print("Rules of the game: ")
    print("1. Player must type numbers from 1 to 100")
    print("2. If a number is divisible by 3, you must type 'Fizz'")
    print("3. If a number is divisible by 5, you must type 'Buzz'")
    print("4. If a number is divisible by 3 and 5, you must type 'FizzBuzz'")
    print("5. You only have 3 lifes")
    print("6. You get 10 points for each right answer")
    print("7. If you type the wrong answer, you loose 1 life and 5 points")
    print("Good luck...")

    score = 0
    lifes = 3
    for n in range(1, 101):
        if lifes > 0:
            r = str(input("Type your answer: "))
            if (n % 3 == 0) and (n % 5 == 0):
                i = 'FizzBuzz'
            elif n % 3 == 0:
                i = 'Fizz'
            elif n % 5 == 0:
                i = 'Buzz'
            else:
                i = n

            if r == str(i):
                print("Correct!")
                score += 10
            else:
                print("Incorrect!")
                score -= 5
                lifes -= 1
            print("Your score is: {}".format(score))
            print("You have {} lifes".format(lifes))
        else:
            print("Game over")
            return

game_fizzbuzz()
