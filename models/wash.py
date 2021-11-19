from colorama import Fore, Style
import getpass
import sys


def cprint(message, color=Fore.WHITE):

    if color == "red":
        print(f"{Fore.RED}{message}{Style.RESET_ALL}", end="")
    elif color == "green":
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}", end="")
    elif color == "yellow":
        print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}", end="")
    elif color == "blue":
        print(f"{Fore.BLUE}{message}{Style.RESET_ALL}", end="")
    elif color == "cyan":
        print(f"{Fore.CYAN}{message}{Style.RESET_ALL}", end="")
    elif color == "magenta":
        print(f"{Fore.MAGENTA}{message}{Style.RESET_ALL}", end="")
    elif color == "lightred":
        print(f"{Fore.LIGHTRED_EX}{message}{Style.RESET_ALL}", end="")
    elif color == "lightyellow":
        print(f"{Fore.LIGHTYELLOW_EX}{message}{Style.RESET_ALL}", end="")
    elif color == "lightwhite":
        print(f"{Fore.LIGHTWHITE_EX}{message}{Style.RESET_ALL}", end="")
    elif color == "lightcyan":
        print(f"{Fore.LIGHTCYAN_EX}{message}{Style.RESET_ALL}", end="")
    elif color == "lightblue":
        print(f"{Fore.LIGHTBLUE_EX}{message}{Style.RESET_ALL}", end="")
    elif color == "gray" or color == "grey":
        print(f"{Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}", end="")
    elif color == "lightgreen":
        print(f"{Fore.LIGHTGREEN_EX}{message}{Style.RESET_ALL}", end="")
    elif color == "lightmagenta":
        print(f"{Fore.LIGHTMAGENTA_EX}{message}{Style.RESET_ALL}", end="")
    else:
        print(message)


def cinput(message, color=Fore.WHITE):

    if color == "red":
        i = input(f"{Fore.RED}{message}{Style.RESET_ALL}")
    elif color == "green":
        i = input(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    elif color == "yellow":
        i = input(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
    elif color == "blue":
        i = input(f"{Fore.BLUE}{message}{Style.RESET_ALL}")
    elif color == "cyan":
        i = input(f"{Fore.CYAN}{message}{Style.RESET_ALL}")
    elif color == "magenta":
        i = input(f"{Fore.MAGENTA}{message}{Style.RESET_ALL}")
    elif color == "lightred":
        i = input(f"{Fore.LIGHTRED_EX}{message}{Style.RESET_ALL}")
    elif color == "lightyellow":
        i = input(f"{Fore.LIGHTYELLOW_EX}{message}{Style.RESET_ALL}")
    elif color == "lightwhite":
        i = input(f"{Fore.LIGHTWHITE_EX}{message}{Style.RESET_ALL}")
    elif color == "lightcyan":
        i = input(f"{Fore.LIGHTCYAN_EX}{message}{Style.RESET_ALL}")
    elif color == "lightblue":
        i = input(f"{Fore.LIGHTBLUE_EX}{message}{Style.RESET_ALL}")
    elif color == "gray" or color == "grey":
        i = input(f"{Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}")
    elif color == "lightgreen":
        i = input(f"{Fore.LIGHTGREEN_EX}{message}{Style.RESET_ALL}")
    elif color == "lightmagenta":
        i = input(f"{Fore.LIGHTMAGENTA_EX}{message}{Style.RESET_ALL}")
    else:
        i = input(message)
    return i

def cstdout(message, color=Fore.WHITE):

    if color == "red":
        sys.stdout.write(f"{Fore.RED}{message}{Style.RESET_ALL}")
    elif color == "green":
        sys.stdout.write(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    elif color == "yellow":
        sys.stdout.write(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
    elif color == "blue":
        sys.stdout.write(f"{Fore.BLUE}{message}{Style.RESET_ALL}")
    elif color == "cyan":
        sys.stdout.write(f"{Fore.CYAN}{message}{Style.RESET_ALL}")
    elif color == "magenta":
        sys.stdout.write(f"{Fore.MAGENTA}{message}{Style.RESET_ALL}")
    elif color == "lightred":
        sys.stdout.write(f"{Fore.LIGHTRED_EX}{message}{Style.RESET_ALL}")
    elif color == "lightyellow":
        sys.stdout.write(f"{Fore.LIGHTYELLOW_EX}{message}{Style.RESET_ALL}")
    elif color == "lightwhite":
        sys.stdout.write(f"{Fore.LIGHTWHITE_EX}{message}{Style.RESET_ALL}")
    elif color == "lightcyan":
        sys.stdout.write(f"{Fore.LIGHTCYAN_EX}{message}{Style.RESET_ALL}")
    elif color == "lightblue":
        sys.stdout.write(f"{Fore.LIGHTBLUE_EX}{message}{Style.RESET_ALL}")
    elif color == "gray" or color == "grey":
        sys.stdout.write(f"{Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}")
    elif color == "lightgreen":
        sys.stdout.write(f"{Fore.LIGHTGREEN_EX}{message}{Style.RESET_ALL}")
    elif color == "lightmagenta":
        sys.stdout.write(f"{Fore.LIGHTMAGENTA_EX}{message}{Style.RESET_ALL}")
    else:
        sys.stdout.write(message)

def cgpass(message, color=Fore.WHITE):

    if color == "red":
        i = getpass.getpass(f"{Fore.RED}{message}{Style.RESET_ALL}")
    elif color == "green":
        i = getpass.getpass(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    elif color == "yellow":
        i = getpass.getpass(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
    elif color == "blue":
        i = getpass.getpass(f"{Fore.BLUE}{message}{Style.RESET_ALL}")
    elif color == "cyan":
        i = getpass.getpass(f"{Fore.CYAN}{message}{Style.RESET_ALL}")
    elif color == "magenta":
        i = getpass.getpass(f"{Fore.MAGENTA}{message}{Style.RESET_ALL}")
    elif color == "lightred":
        i = getpass.getpass(f"{Fore.LIGHTRED_EX}{message}{Style.RESET_ALL}")
    elif color == "lightyellow":
        i = getpass.getpass(f"{Fore.LIGHTYELLOW_EX}{message}{Style.RESET_ALL}")
    elif color == "lightwhite":
        i = getpass.getpass(f"{Fore.LIGHTWHITE_EX}{message}{Style.RESET_ALL}")
    elif color == "lightcyan":
        i = getpass.getpass(f"{Fore.LIGHTCYAN_EX}{message}{Style.RESET_ALL}")
    elif color == "lightblue":
        i = getpass.getpass(f"{Fore.LIGHTBLUE_EX}{message}{Style.RESET_ALL}")
    elif color == "gray" or color == "grey":
        i = getpass.getpass(f"{Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}")
    elif color == "lightgreen":
        i = getpass.getpass(f"{Fore.LIGHTGREEN_EX}{message}{Style.RESET_ALL}")
    elif color == "lightmagenta":
        i = getpass.getpass(f"{Fore.LIGHTMAGENTA_EX}{message}{Style.RESET_ALL}")
    else:
        i = getpass.getpass(message)
    return i
    

