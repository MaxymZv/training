from colorama import Fore, Style
from time import sleep


"""This is basic training script for traffic light simulator, it`s works with colorama and time modules, specially sleep function for pause between color changes."""


#Start of the function and main code
def traffic_light(color):
    if color == "red":
        return f"{Fore.RED}Stop{Style.RESET_ALL}" #using colorama for showing color, simulating traffic light
    elif color == "yellow":
        return f"{Fore.YELLOW}Caution{Style.RESET_ALL}"
    elif color == "green":
        return f"{Fore.GREEN}Go{Style.RESET_ALL}"
    else:
        return f"{Fore.WHITE}Invalid color{Style.RESET_ALL}"
    

#Main use of that function
for color in ["red", "yellow", "green"]:
    print(traffic_light(color))
    sleep(2)