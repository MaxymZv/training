from time import sleep


def user_input(user_input):
    if not user_input.strip():  # checking if input is empty
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, args




def stop_timer():
    start = 0
    print('It`s a time tracker!')
    while True:
        user_input = input('Type "start" to begin or "exit" to quit: ').strip().lower()
        if user_input == 'exit':
            print('Exiting the timer.')
            break
        elif user_input == 'start':
            start += 1
            print(f'Timer started at {start} seconds.')
        elif user_input == 'stop':
            print(f'Timer stopped at {start} seconds.')
            break
        else:
            print('Invalid command. Please type "start" to begin or "exit" to quit.')
            continue
    print('Timer has been stopped.')


if __name__ == "__main__":
    stop_timer()


