from src.encryptor import Encryptor
from src.file_encryptor import FileEncryptor
from src.banner import *
from src.aes_encryptor import AES_encryptor
import getpass
import os
import shutil
from base64 import b64encode, b64decode

class Action:

    def __init__(self):
        
        self.e_obj = Encryptor()
        self.f_obj = FileEncryptor()
        self.a_obj = AES_encryptor()



    # This Function ask the user to input password !
    def get_password(self, retype=True):

        if retype:

            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: ")

            retype_password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Retype Password{aqua}: ")


            if password == "": 
                
                print(f"{aqua}[{red}!{aqua}] {red}Please Enter vaild password")
                exit(1)

            if password == retype_password:

                key = self.a_obj.password_to_aes_key(password)

                return key

            else:

                print(f"\n{aqua}[{red}!{aqua}] {red}Password Dont Match{aqua}!")
                exit(1)

        elif not retype:

            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: ")

            key = self.a_obj.password_to_aes_key(password)

            return key

    # This function check if file is exists or not
    def check_file(self, filepath):

        try:
            open(filepath,"rb")

        except FileNotFoundError:

            print(f"{aqua}[{red}!{aqua}] {red}File Not found {aqua}!")
            exit(1)



    # This function check if the path is directory or file 
    def check_dir(self, path):

        if not os.path.isdir(path):

            pass

        elif os.path.isdir(path):

            print(f"{aqua}[{red}!{aqua}] {red}This is not file is a directory {aqua}!")
            exit(1)


    # This function copy files
    def copy_file(self, filepath):

        filename = os.path.basename(filepath)

        if "/" in filepath:

            c_filepath = os.path.dirname(filepath) + "/C_" + filename

        else:

            c_filepath = "C_" + filename


        shutil.copy(filepath, c_filepath)

        return c_filepath


    # This function if he want overwrite file with encryption or not
    def overwrite_action(self):

        # Just give the user some spcae LOL !

        answers_y = ["y", "yes", "ye","yep", "yah", "ya", "yeah"]

        answers_n = ["n", "no", "nope", "nah"]


        while True:

            inp = input(f"{aqua}[{red}?{aqua}]{red} Do you want overwrite it {aqua}({red}y{aqua}/{red}n{aqua}):{red} ").lower().strip()

            if inp in answers_y: return "y"; break

            elif inp in answers_n: return "n"; break

            else: continue




    # This function handle AES encryption or decrption
    def aes_action(self, msg, encryption=True):

        if encryption:

            encrypted_msg = self.a_obj.encrypt(msg.encode(), self.get_password())

            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {b64encode(encrypted_msg).decode()}")

            
        elif not encryption:
            
            try:
                decrypted_msg = self.a_obj.decrypt(b64decode(msg.encode()),self.get_password(False))

                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}")

            except Exception:

                print(f"{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!")
                exit(1)


    # This function handle AES file Encryption 
    def aes_file_action(self, path, encryption=True):

        self.check_dir(path)

        self.check_file(path)


        if encryption:

            overwrite_answer = self.overwrite_action()

            if  overwrite_answer == "y":

                encrypted_file = self.a_obj.encrypt_file(path, self.get_password())
                print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!")

            elif overwrite_answer == "n":

                c_filepath = self.copy_file(path)

                encrypted_file = self.a_obj.encrypt_file(c_filepath, self.get_password())
                print(f"{aqua}[{red}${aqua}] {red}{c_filepath} Encrypted successfully {aqua}!")



        elif not encryption:
            
            try:
                decrypted_file = self.a_obj.decrypt_file(path, self.get_password(False))

                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!")

            except:
                print(f"\n{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!")
                exit(1)


    # This function handle RSA encryption and decryption!
    def rsa_action(self, msg, encryption=True):

        if encryption:
            
            encrypted_msg = self.e_obj.rsa_encrypt(msg.encode("utf-8"))
            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {encrypted_msg}")
        

        elif not encryption:

            try:
                decrypted_msg = self.e_obj.rsa_decrypt(msg.encode("utf-8"))
                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}")

            
            except ValueError:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!")
                exit(1)
            


    # This function handle RSA file Encryption and Decryption
    def rsa_file_action(self, path, encryption=True):

        self.check_dir(path)

        self.check_file(path)


        if encryption:

            overwrite_answer = self.overwrite_action()

            if overwrite_answer == "y":

                encrypted_file = self.f_obj.rsa_encrypt_file(path)
                print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!")

            elif overwrite_answer == "n":

                c_filepath = self.copy_file(path)

                encrypted_file = self.f_obj.rsa_encrypt_file(c_filepath)
                print(f"{aqua}[{red}${aqua}] {red}{c_filepath} Encrypted successfully {aqua}!")


        elif not encryption:
            
            try:
                decrypted_file = self.f_obj.rsa_decrypt_file(path)
                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!")

            except ValueError:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!")
                exit(1)




    # This function handle RSA encryption and decryption by loading key !
    def rsa_action_load(self, msg, path, encryption=True):

        self.check_dir(path)

        self.check_file(path)

        if encryption:

            encrypted_msg = self.e_obj.rsa_encrypt_load(msg.encode("utf-8"), path)
            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {encrypted_msg}")

        elif not encryption:

            try:
                decrypted_msg = self.e_obj.rsa_decrypt_load(msg.encode("utf-8"), path)
                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}")

            except ValueError:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!")
                exit(1)


    # This function handle RSA file Encryption and Decryption by loading key !
    def rsa_file_action_load(self, path, key_path, encryption=True):

        self.check_dir(path)

        self.check_file(path)

        if encryption:

            overwrite_answer = self.overwrite_action()

            if overwrite_answer == "y":

                encrypted_file = self.f_obj.rsa_encrypt_file_load(path, key_path)
                print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!")


            elif overwrite_answer == "n":

                c_filepath = self.copy_file(path)

                encrypted_file = self.f_obj.rsa_encrypt_file_load(c_filepath, key_path)
                print(f"{aqua}[{red}${aqua}] {red}{c_filepath} Encrypted successfully {aqua}!")

        elif not encryption:
            
            try:
                decrypted_file = self.f_obj.rsa_decrypt_file_load(path, key_path)
                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!")

            except:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!")
                exit(1)
