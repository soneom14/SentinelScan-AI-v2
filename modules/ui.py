from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)


def show_banner():
    fig = Figlet(font="slant")

    print(Fore.CYAN + fig.renderText("SentinelScan-AI"))
    print(Fore.YELLOW + "=" * 80)
    print(Fore.GREEN + " Advanced AI Powered Vulnerability Scanner")
    print(Fore.YELLOW + "=" * 80)
    print()


def success(text):
    print(Fore.GREEN + "[+] " + text)


def error(text):
    print(Fore.RED + "[-] " + text)


def warning(text):
    print(Fore.YELLOW + "[!] " + text)


def info(text):
    print(Fore.CYAN + "[*] " + text)


def separator():
    print(Fore.CYAN + "═" * 80)