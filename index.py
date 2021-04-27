from random import randint

def computer_guess(num):
    low = 1
    high = 1000
    guess = randint(1, 1000)
    while guess != num:
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
            print("Too big!")
        elif guess < num:
            low = guess + 1
            print("Too small!")

        guess = (low+high)//2

    print("The computer guessed", guess, "and it was correct!")


def main():
    num = int(input("Enter a number: "))
    if num < 1 or num > 1000:
        print("Must be in range [1, 1000]")
    else:
        computer_guess(num)

if __name__ == '__main__':
    main()
