from colorama import Fore, Style

def title(text):

    print()

    print(Fore.CYAN + "=" * 70)
    print(Fore.YELLOW + text.center(70))
    print(Fore.CYAN + "=" * 70)