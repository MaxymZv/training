from time import sleep


#This script just a simple timer, it works with sleep function from time module.
def timer():
    seconds = int(input('Enter amount of seconds: '))
    if seconds <= 0:
        print("Please enter a positive number.")
        return
    for i in range(seconds, 0, -1):
        print(f"Time left: {i} seconds", end='\r')
        sleep(1)
    print('Time`s up!', end='\t\n')

if __name__ == "__main__":
    timer()