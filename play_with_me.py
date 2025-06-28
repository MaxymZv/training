from random import randint


count_wins = 0

count_losses = 0


def game():
    global count_wins, count_losses
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    choices = ['rock', 'paper', 'scissors']
    if user_choice not in choices:
        print('Invalid choice!')
        return
    computer_choice = choices[randint(0, 2)]
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        count_wins += 1

    else:
        print("You lose!")
        count_losses += 1



game()

print(f"Total wins: {count_wins}")
print(f"Total losses: {count_losses}")
    
