from random import choice
from .styles import *

sepChars = "=-*~+._"
version = f"{aqua}v{red}1{aqua}.{red}0{aqua}.{red}5"


def pickRandSepChar():
        return choice(sepChars)

def outputBanner():
        print(banner)

banner = f"""
   {red} ____          _  ____ _       _               
   |  _ \ ___  __| |/ ___(_)_ __ | |__   ___ _ __ 
   | |_) / _ \/ _` | |   | | '_ \| '_ \ / _ \ '__|
   |  _ <  __/ (_| | |___| | |_) | | | |  __/ |   
   |_| \_\___|\__,_|\____|_| .__/|_| |_|\___|_|   
                           |_|              {version}                         

   {red}Professional Encryption {aqua}/{red} Decryption program {aqua}!

   {" " * 5}{aqua}{pickRandSepChar() * 35}{red}{reset}

"""             


if __name__ == "__main__":
    outputBanner()
