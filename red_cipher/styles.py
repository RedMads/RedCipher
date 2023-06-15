## xP0: i know this file is boring and may look useless, but i feel there is a way to improve it.
###     the purpose of this file is to prettify the calls of printing stuff "(info, errors)" so that each print call does clear it's meaning by reading the function only

from colorama import Fore


red = Fore.RED
aqua = Fore.CYAN
blink = "\033[5m"
reset = Fore.RESET


def pprint(text, sign="!"):
    fmt = f"{aqua}[{red}{sign}{aqua}]{red} TEXT_PLACEHOLDER {aqua}!{reset}"
    text = fmt.replace("TEXT_PLACEHOLDER", text)
    print(text)

# xP0: OK i know.. naming is only to cover the function purpose
def pinfo(text):
    pprint(text)

def perror(text):
    pprint(text)
