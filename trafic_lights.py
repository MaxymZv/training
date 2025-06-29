from colorama import Fore, Style
from time import sleep

def traffic_light(color):
    if color == "red":
        return f"{Fore.RED}Stop{Style.RESET_ALL}"
    elif color == "yellow":
        return f"{Fore.YELLOW}Caution{Style.RESET_ALL}"
    elif color == "green":
        return f"{Fore.GREEN}Go{Style.RESET_ALL}"
    else:
        return f"{Fore.WHITE}Invalid color{Style.RESET_ALL}"
    


for color in ["red", "yellow", "green"]:
    print(traffic_light(color))
    sleep(2)