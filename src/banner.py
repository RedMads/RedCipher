from colorama import Fore

red = Fore.RED
aqua = Fore.CYAN
blink = "\033[5m"
reset = "\033[0m"
b = f"""
{red}  ____          _  ____ _       _               
 |  _ \ ___  __| |/ ___(_)_ __ | |__   ___ _ __ 
 | |_) / _ \/ _` | |   | | '_ \| '_ \ / _ \ '__|
 |  _ <  __/ (_| | |___| | |_) | | | |  __/ |   
 |_| \_\___|\__,_|\____|_| .__/|_| |_|\___|_|   
                         |_|               

               {aqua}-={red} By RedMad :$ {aqua}=-

        {aqua}-={red} https://github.com/RedMads/ {aqua}=-

     {red}Professional Encryption {aqua}/{red} Decryption tool {aqua}!

    {aqua}============================================{red}

"""



def banner():
    print(b)
