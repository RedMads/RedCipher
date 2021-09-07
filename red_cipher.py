"""
Hello Guys im redmad :$ today i made this super powerful Script !!!

Privacy is right for every human in the world, 
red cipher help you encrypt / decrypt messages or files with two secure and strong algorithms, 
the first one < AES > and the second < RSA > with many modes and options !


special thanks to:
    
    @yytv_ & @wzxmpl 

    and other friends !!!


- RedMad :$

"""
from src.encryptor import Encryptor
from src.file_encryptor import FileEncryptor
from src.actions import Action
from src.banner import *
import sys, getpass, argparse
from os import *



class Main:


    def __init__(self, KeySize=8192):

        self.key_size = KeySize

        self.e_obj = Encryptor()
        self.f_obj = FileEncryptor()
        self.a_obj = Action()

        self.mode = ["encryption", "decryption"]
        self.algrothims = ["rsa","aes"]

        self.enc_mode = None
        self.msg = ""
        self.algo = None
        self.file_mode = False
        self.file_path = None
        self.load_mode = False
        self.load_path = None
        
        self.show_help = True
        self.help = None
        

    def check_args(self):

        parser = argparse.ArgumentParser()
        
        
        parser.add_argument("-e", "--encrypt", required=False, type=str, metavar="", help="-e < AES, RSA > : to encrypt")
        parser.add_argument("-d", "--decrypt", required=False, type=str, metavar="", help="-d < AES, RSA > : to decrypt")
        parser.add_argument("-f","--file", required=False, type= str, metavar="", help="-f < FILE PATH > : specify file path")
        parser.add_argument("-m", "--message", required=False, type=str, metavar="", help="-m < MESSAGE > : specify message")
        parser.add_argument("-g", "--generate", required=False, type=int, metavar="", help="-g < BYTES SIZE > : generate rsa keys")
        parser.add_argument("-l", "--load", required=False, type=str, metavar="", help="-l < KEY PATH > : load key file to encrypt or decrypt")
        

        args = parser.parse_args()


        if args.encrypt:

            self.enc_mode = self.mode[0]
            self.algo = args.encrypt
            self.show_help = False
            

            if str(self.algo).lower() in self.algrothims:
                
                pass

            else:
                parser.print_help()

            
        elif args.decrypt:

            self.enc_mode = self.mode[1]
            self.algo = args.decrypt
            self.show_help = False
 

            if str(self.algo).lower() in self.algrothims:

                pass

            else:

                parser.print_help()


        if args.message:

            self.msg = args.message
            self.show_help = False
 

        elif args.file:

            self.file_mode = True
            self.file_path = args.file
            self.show_help = False
 
        if args.generate:

            self.show_help = False

            if not self.e_obj.check_files():

                self.e_obj.generate_keys()

            else:

                while True:

                    inp = input(f"{aqua}[{red}?{aqua}]{red} you have keys in {self.e_obj.keys_dir} do you want overwrite it {aqua}({red}y{aqua}/{red}n{aqua}):{red} ")

                    if inp == "y":
                        
                        self.e_obj.generate_keys(True, args.generate)
                        print(f"{aqua}[{red}${aqua}]{red} keys successfully generated {self.e_obj.keys_dir}")
                        break

                    elif inp == "n":

                        exit(1)

                    else: continue




        if args.load:

            self.load_mode = True
            self.load_path = args.load
            self.show_help = False

        if self.show_help:

            parser.print_help()



    def action(self):
        
        if str(self.algo).lower() == "aes":
            
            if self.file_mode:

                if self.enc_mode == self.mode[0]:

                    self.a_obj.aes_file_action(self.file_path)

                elif self.enc_mode == self.mode[1]:

                    self.a_obj.aes_file_action(self.file_path, False)

            elif not self.file_mode:

                if self.enc_mode == self.mode[0]:
                    self.a_obj.aes_action(self.msg)

                elif self.enc_mode == self.mode[1]:

                    self.a_obj.aes_action(self.msg, False)


        elif str(self.algo).lower() == "rsa":

            if self.file_mode:
                
                if self.enc_mode == self.mode[0]:

                    if self.load_mode:

                        self.a_obj.rsa_file_action_load(self.file_path, self.load_path)

                    elif not self.load_mode:
                        self.a_obj.rsa_file_action(self.file_path)

                elif self.enc_mode == self.mode[1]:

                    if self.load_path:

                        self.a_obj.rsa_file_action_load(self.file_path, self.load_path, False)
                    
                    elif not self.load_path:

                        self.a_obj.rsa_file_action(self.file_path, False)

            elif not self.file_mode:

                if self.enc_mode == self.mode[0]:

                    if self.load_mode:
                        self.a_obj.rsa_action_load(self.msg, self.load_path)

                    elif not self.load_mode:
                        self.a_obj.rsa_action(self.msg)

                elif self.enc_mode == self.mode[1]:

                    if self.load_mode:

                        self.a_obj.rsa_action_load(self.msg, self.load_path, False)
                        
                    elif not self.load_mode:
                        self.a_obj.rsa_action(self.msg, False)




if __name__ == "__main__":

    banner()

    m_obj = Main()
    
    m_obj.e_obj.check_dir()
    m_obj.e_obj.check_files()
    m_obj.check_args()
    m_obj.action()
