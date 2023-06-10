from random import choice
from colorama import Fore


red = Fore.RED
aqua = Fore.CYAN
blink = "\033[5m"
reset = Fore.RESET

sepChars = "=-*~+._"
version = f"{aqua}v{red}1{aqua}.{red}0{aqua}.{red}5"

banner = f"""
   {red} ____          _  ____ _       _               
   |  _ \ ___  __| |/ ___(_)_ __ | |__   ___ _ __ 
   | |_) / _ \/ _` | |   | | '_ \| '_ \ / _ \ '__|
   |  _ <  __/ (_| | |___| | |_) | | | |  __/ |   
   |_| \_\___|\__,_|\____|_| .__/|_| |_|\___|_|   
                           |_|              {version}                         

   {red}Professional Encryption {aqua}/{red} Decryption program {aqua}!

   {" " * 5}{aqua}{pickRandSepChar() * 35}{red}

"""             


def pickRandSepChar():
        return choice(sepChars)

def outputBanner():
        print(banner)


if __name__ == "__main__":
    outputBanner()
