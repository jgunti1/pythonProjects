import random

def main():
    startRange = int(input("Start Range: "))
    endRange = int(input("End Range: "))
    ranNum = random.randint(startRange,endRange) 
    guess = int(input("Guess: "))
    guesses = 0
    if (guess > endRange or guess <startRange):
        guesses+=1
        print("Try again! Guess is outside of range.")
        print(f"Range: {startRange} to {endRange}")
    elif (guess < ranNum):
        guesses += 1
        startRange = guess
        print("Try again! You guessed too small.")
        print(f"Range: {startRange} to {endRange}")
    elif (guess > ranNum):
        guesses +=1
        endRange = guess
        print("Try again! You guessed too big.")
        print(f"Range: {startRange} to {endRange}")
    elif (guess == startRange or guess == endRange):
        guesses+=1
        print("Try again! You guessed the range starting numbers.")
        print(f"Range: {startRange} to {endRange}")
    else:
        print(f"That's the right number! You guessed {ranNum} in {guess} guesses!")
    while (guess != ranNum):
        guess = int(input("Guess: "))
        if (guess > endRange or guess <startRange):
            print("Try again! Guess is outside of range.")
            print(f"Range: {startRange} to {endRange}")
        elif (guess < ranNum):
            guesses += 1
            startRange = guess
            print("Try again! You guessed too small.")
            print(f"Range: {startRange} to {endRange}")
        elif (guess > ranNum):
            guesses +=1
            endRange = guess
            print("Try again! You guessed too big.")
            print(f"Range: {startRange} to {endRange}")
        elif (guess == startRange or guess == endRange):
            guesses+=1
            print("Try again! You guessed the range starting numbers.")
            print(f"Range: {startRange} to {endRange}")
        else:
            guesses += 1
            print(f"That's the right number! You guessed {ranNum} in {guesses} guesses!")

if __name__ == "__main__":
    main()
