from .rsa_encryptor import RsaEncryptor
from .banner import *
from .aes_encryptor import AesEncryptor
from .handle_json import HandleJson
from .utils import *
from base64 import b64encode, b64decode
import getpass
import os
import shutil
import sys


class Action:
    def __init__(self):        
        self.e_obj = RsaEncryptor()
        self.a_obj = AesEncryptor()
        self.h_obj = HandleJson()

        self.h_obj.loadJson()
        self.settings = self.h_obj.getSettings()


    # This Function ask the user to input password !
    def getPassword(self, retype=True):
        if retype:
            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: {reset}")
            retype_password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Retype Password{aqua}: {reset}")

            if password == "": 
                print(f"{aqua}[{red}!{aqua}] {red}Please Enter vaild password{reset}")
                exitProg(1)

            if password == retype_password:
                key = self.a_obj.password2AesKey(password)
                return key
            else:
                print(f"\n{aqua}[{red}!{aqua}] {red}Password Doesnt Match{aqua}!{reset}")
                exitProg(1)

        else:
            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: {reset}")
            key = self.a_obj.password2AesKey(password)
            return key


    def checkExt(self, settings):
        if not settings["extension"]:
            print(f"{aqua}[{red}!{aqua}] {red}Extension needs to be specified {aqua}!{reset}")
            exitProg(1)


    def checkFile(self, filepath, message="File not found"):
        try:
            open(filepath, "rb").close()

        except FileNotFoundError:
            print(f"{aqua}[{red}!{aqua}] {red}{message}{aqua} !{reset}")
            exitProg(1)


    def checkDir(self, path):
        if os.path.isdir(path):
            print(f"{aqua}[{red}!{aqua}] {red}This is not file is a directory {aqua}!{reset}")
            exitProg(1)


    def checkOS(self):
        if os.name == "nt":
            return ("windows", "\\")
        else:
            return ("linux", "/")


    def copyFile(self, filepath):
        filename = os.path.basename(filepath)
        slash = self.checkOS()[1]

        if slash in filepath:
            c_filepath = os.path.dirname(filepath) + slash + "C_" + filename
        else:
            c_filepath = "C_" + filename

        shutil.copy(filepath, c_filepath)
        return c_filepath


    def checkPermission(self, filepath):
        try:
            open(filepath, "rb+").close()

        except PermissionError:
            print(f"{aqua}[{red}!{aqua}]{red} {filepath} Permission denied {aqua}!{reset}")
            exitProg(1)


    def checkAll(self, filepath, settings):
        self.checkDir(filepath)
        self.checkFile(filepath)
        self.checkPermission(filepath)
        self.checkExt(settings)


    def overwriteAction(self):
        # Just give the user some spcae LOL !
        answers_y = ["y", "yes", "ye","yep", "yah", "ya", "yeah"]

        while True:
            #xP0: Defaults to "NO"/Don't overwrite
            inp = input(f"{aqua}[{red}?{aqua}]{red} Do you want overwrite it {aqua}({red}y{aqua}/{red}N{aqua}): {red}").lower().strip()

            if inp not in answers_y:
                return "n"
            else:
                return "y"


    # useful function for warning the user if he trys
    # to generate new keys and he have keys before
    def overwriteKeysAction(self, keySize:int):
        # Just give the user some spcae LOL ! *2*
        answers_y = ["y", "yes", "ye","yep", "yah", "ya", "yeah"]

        while True:
            #xP0: Defaults to "NO"/Don't overwrite
            inp = input(f"{aqua}[{red}?{aqua}]{red} you have keys in {self.e_obj.keys_dir} do you want overwrite it {aqua}({red}y{aqua}/{red}N{aqua}): {red} {reset}")

            if inp not in answers_y:
                exitProg(1)

            self.e_obj.generateRsaKeys(True, keySize)
            print(f"{aqua}[{red}${aqua}]{red} keys successfully generated {self.e_obj.keys_dir}{reset}")
            break


    def rsaKeyMinAction(self, keySize:int):
        if keySize < 1024:
            print(f"{aqua}[{red}!{aqua}] {red}Key size is less than 1024 bits{aqua}!{reset}")
            exitProg(1)


    def checkPubKeyDec(self, keyPath:str):
        if "public" in keyPath:
            print(f"{aqua}[{red}!{aqua}] {red}Cannot decrypt with public key{aqua}!{reset}")
            exitProg(1)


    def checkPrivkeyEnc(self, keyPath:str):
        if "private" in keyPath:
            print(f"{aqua}[{red}!{aqua}] {red}Cannot encrypt with private key{aqua}!{reset}")
            exitProg(1)


    def aesAction(self, msg, encryption=True):
        if encryption:
            encrypted_msg = self.a_obj.aesEncrypt(msg.encode(), self.getPassword())
            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {b64encode(encrypted_msg).decode()}{reset}")

        else:            
            try:
                decrypted_msg = self.a_obj.aesDecrypt(b64decode(msg.encode()),self.getPassword(False))
                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}{reset}")

            except ValueError:
                print(f"{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!{reset}")
                exitProg(1)


    def aesFileAction(self, path, encryption=True):
        self.checkAll(path, self.settings)

        if encryption:
            overwrite_answer = self.overwriteAction()
            if  overwrite_answer == "y":
                self.a_obj.aesEncryptFile(path, self.getPassword())
                print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully (file overwritten){aqua}!{reset}")

            elif overwrite_answer == "n":
                c_filepath = self.copyFile(path)
                self.a_obj.aesEncryptFile(c_filepath, self.getPassword())
                print(f"{aqua}[{red}${aqua}] {red}{c_filepath} Encrypted successfully {aqua}!{reset}")

        else:
            try:
                self.a_obj.aesDecryptFile(path, self.getPassword(False))
                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!{reset}")

            except ValueError:
                print(f"\n{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!{reset}")
                exitProg(1)


    def rsaAction(self, msg:str, keyPath:str, encryption=True):
        if encryption:
            self.checkPrivkeyEnc(keyPath)
            encrypted_msg = self.e_obj.rsaEncrypt(msg.encode("utf-8"), keyPath)[1]
            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {b64encode(encrypted_msg).decode()}{reset}")

        else:
            self.checkPubKeyDec(keyPath)
            try:
                decrypted_msg = self.e_obj.rsaDecrypt(b64decode(msg.encode("utf-8")), keyPath)[1]
                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}{reset}")

            except ValueError:
                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!{reset}")
                exitProg(1)


    def rsaFileAction(self, path:str, keyPath:str, encryption=True):
        self.checkAll(path, self.settings)

        if encryption:
            self.checkPrivkeyEnc(keyPath)
            overwrite_answer = self.overwriteAction()
            
            if overwrite_answer == "y":
                self.e_obj.rsaEncryptFile(path, keyPath)
                print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully (file overwritten){aqua}!{reset}")

            elif overwrite_answer == "n":
                c_filepath = self.copyFile(path)
                self.e_obj.rsaEncryptFile(c_filepath, keyPath)
                print(f"{aqua}[{red}${aqua}] {red}{c_filepath} Encrypted successfully {aqua}!{reset}")

        else:
            self.checkPubKeyDec(keyPath)
            try:
                self.e_obj.rsaDecryptFile(path, keyPath)
                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!{reset}")

            except ValueError:
                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!{reset}")
                exitProg(1)
