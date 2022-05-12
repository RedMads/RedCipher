from .rsa_encryptor import RsaEncryptor
from .banner import *
from .aes_encryptor import AesEncryptor
from base64 import b64encode, b64decode
import getpass
import os
import shutil
import sys

class Action:

    def __init__(self):
        
        self.e_obj = RsaEncryptor()
        self.a_obj = AesEncryptor()



    # This Function ask the user to input password !
    def getPassword(self, retype=True):

        if retype:
            
            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: {reset}")

            retype_password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Retype Password{aqua}: {reset}")


            if password == "": 
                
                print(f"{aqua}[{red}!{aqua}] {red}Please Enter vaild password{reset}")
                sys.exit(1)

            if password == retype_password:

                key = self.a_obj.password2AesKey(password)

                return key

            else:

                print(f"\n{aqua}[{red}!{aqua}] {red}Password Dont Match{aqua}!{reset}")
                sys.exit(1)

        elif not retype:

            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: {reset}")

            key = self.a_obj.password2AesKey(password)

            return key

    # This function check if file is exists or not
    def checkFile(self, filepath, message="File not found"):

        try:
            open(filepath,"rb")

        except FileNotFoundError:

            print(f"{aqua}[{red}!{aqua}] {red}{message}{aqua} !{reset}")
            sys.exit(1)



    # This function check if the path is directory or file 
    def checkDir(self, path):

        if not os.path.isdir(path):

            pass

        elif os.path.isdir(path):

            print(f"{aqua}[{red}!{aqua}] {red}This is not file is a directory {aqua}!{reset}")
            sys.exit(1)


    # simple function to check what platform program run at
    def checkOs(self):

        if os.name == "nt": return "windows", "\\"

        else: return "linux", "/"


    # This function copy files
    def copyFile(self, filepath):

        filename = os.path.basename(filepath)

        slash = self.checkOs()[1]

        if slash in filepath:

            c_filepath = os.path.dirname(filepath) + slash + "C_" + filename

        else:

            c_filepath = "C_" + filename


        shutil.copy(filepath, c_filepath)

        return c_filepath


    # simple function check file permssion !
    def checkPermission(self, filepath):

        try:
            open(filepath, "rb+").close()

        except PermissionError:

            print(f"{aqua}[{red}!{aqua}]{red} {filepath} Permission denied {aqua}!{reset}")
            sys.exit(1)



    # simple function for check multi checks in one call !
    def checkAll(self, filepath):

        self.checkDir(filepath)
        self.checkFile(filepath)
        self.checkPermission(filepath)
        



    # This function if he want overwrite file with encryption or not
    def overwriteAction(self):

        # Just give the user some spcae LOL !

        answers_y = ["y", "yes", "ye","yep", "yah", "ya", "yeah"]

        answers_n = ["n", "no", "nope", "nah"]


        while True:

            inp = input(f"{aqua}[{red}?{aqua}]{red} Do you want overwrite it {aqua}({red}y{aqua}/{red}n{aqua}): {red}").lower().strip()

            if inp in answers_y: return "y"; break

            elif inp in answers_n: return "n"; break

            else: continue


    # useful function for warning the user if he trys
    # to generate new keys and he have keys before
    def overwriteKeysAction(self, keySize:int):

        while True:

            inp = input(f"{aqua}[{red}?{aqua}]{red} you have keys in {self.e_obj.keys_dir} do you want overwrite it {aqua}({red}y{aqua}/{red}n{aqua}): {red} {reset}")

            if inp == "y":
                        
                self.e_obj.generateRsaKeys(True, keySize)
                print(f"{aqua}[{red}${aqua}]{red} keys successfully generated {self.e_obj.keys_dir}{reset}")
                break

            elif inp == "n": sys.exit(1)

            else: continue

    
    # function output message to user if he try generate key less than 1024 bit
    def rsaKeyMinAction(self, keySize:int):

        if keySize < 1024:

            print(f"{aqua}[{red}!{aqua}] {red}Key size is less than 1024 bits{aqua}!{reset}")
            sys.exit(1)


    # function to check if user trys to decrypt with public key
    def checkPubKeyDec (self, keyPath:str) -> None:

        if "public" in keyPath:
            print(f"{aqua}[{red}!{aqua}] {red}Cannot decrypt with public key{aqua}!{reset}")
            sys.exit(1)


    # function to check if user trys to encrypt with private key
    def checkPrivkeyEnc(self, keyPath:str) -> None:

        if "private" in keyPath:
            print(f"{aqua}[{red}!{aqua}] {red}Cannot encrypt with private key{aqua}!{reset}")
            sys.exit(1)
        



    # This function handle AES encryption or decrption
    def aesAction(self, msg, encryption=True):

        if encryption:

            encrypted_msg = self.a_obj.aesEncrypt(msg.encode(), self.getPassword())

            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {b64encode(encrypted_msg).decode()}{reset}")

            
        elif not encryption:
            
            try:
                decrypted_msg = self.a_obj.aesDecrypt(b64decode(msg.encode()),self.getPassword(False))

                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}{reset}")

            except ValueError:

                print(f"{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!{reset}")
                sys.exit(1)


    # This function handle AES file Encryption 
    def aesFileAction(self, path, encryption=True):

        self.checkAll(path)


        if encryption:

            overwrite_answer = self.overwriteAction()

            if  overwrite_answer == "y":

                self.a_obj.aesEncryptFile(path, self.getPassword())
                print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!{reset}")

            elif overwrite_answer == "n":

                c_filepath = self.copyFile(path)

                self.a_obj.aesEncryptFile(c_filepath, self.getPassword())
                print(f"{aqua}[{red}${aqua}] {red}{c_filepath} Encrypted successfully {aqua}!{reset}")



        elif not encryption:
            
            try:
                self.a_obj.aesDecryptFile(path, self.getPassword(False))

                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!{reset}")

            except ValueError:
                print(f"\n{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!{reset}")
                sys.exit(1)


    # This function handle RSA encryption and decryption!
    def rsaAction(self, msg:str, keyPath:str, encryption=True):

        if encryption:
            
            self.checkPrivkeyEnc(keyPath)
            
            encrypted_msg = self.e_obj.rsaEncrypt(msg.encode("utf-8"), keyPath)[1]
            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {b64encode(encrypted_msg).decode()}{reset}")
        

        elif not encryption:

            self.checkPubKeyDec(keyPath)

            try:
                decrypted_msg = self.e_obj.rsaDecrypt(b64decode(msg.encode("utf-8")), keyPath)[1]
                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}{reset}")

            
            except ValueError:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!{reset}")
                sys.exit(1)
            


    # This function handle RSA file Encryption and Decryption
    def rsaFileAction(self, path:str, keyPath:str, encryption=True):

        self.checkAll(path)


        if encryption:

            self.checkPrivkeyEnc(keyPath)

            overwrite_answer = self.overwriteAction()

            if overwrite_answer == "y":

                self.e_obj.rsaEncryptFile(path, keyPath)
                print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!{reset}")

            elif overwrite_answer == "n":

                c_filepath = self.copyFile(path)

                self.e_obj.rsaEncryptFile(c_filepath, keyPath)
                print(f"{aqua}[{red}${aqua}] {red}{c_filepath} Encrypted successfully {aqua}!{reset}")


        elif not encryption:

            self.checkPubKeyDec(keyPath)
            
            try:
                self.e_obj.rsaDecryptFile(path, keyPath)
                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!{reset}")

            except ValueError:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!{reset}")
                sys.exit(1)
