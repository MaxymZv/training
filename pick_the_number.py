from random import randint


def pick_the_number():
    number = randint(0, 10)
    attempts = 0
    print("Guess the number between 0 and 10!")
    while True:
        try:
            pick = int(input('Are you lucky?: '))
            attempts += 1
            if pick < 0 or pick > 10:
                print("Please pick a number between 0 and 10.")
                continue
            if pick == number:
                print(f'Today is you lucky day! The number was {number}, it only took you {attempts} attempts.')
                break
            elif pick < number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
            continue


if __name__ == "__main__":
    pick_the_number()