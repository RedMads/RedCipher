from src.encryptor import Encryptor
from src.file_encryptor import FileEncryptor
from src.banner import *
import getpass
import os

class Action:

    def __init__(self):
        
        self.e_obj = Encryptor()
        self.f_obj = FileEncryptor()




    def get_password(self, retype=True):

        if retype:

            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: ")

            retype_password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Retype Password{aqua}: ")

            if password == retype_password:

                key = self.e_obj.password_to_fernet_key(password)

                return key

            else:

                print(f"\n{aqua}[{red}!{aqua}] {red}Password Dont Match{aqua}!")
                exit(1)

        elif not retype:

            password = getpass.getpass(f"{aqua}[{red}${aqua}] {red}Enter Password{aqua}: ")

            key = self.e_obj.password_to_fernet_key(password)

            return key


    def check_file(self, filepath):

        try:
            open(filepath,"rb")

        except FileNotFoundError:

            print(f"{aqua}[{red}!{aqua}] {red}File Not found {aqua}!")
            exit(1)


    def check_dir(self, path):

        if not os.path.isdir(path):

            pass

        elif os.path.isdir(path):

            print(f"{aqua}[{red}!{aqua}] {red}This is not file is a directory {aqua}!")
            exit(1)


    def aes_action(self, msg, encryption=True):

        if encryption:

            encrypted_msg = self.e_obj.fernet_encrypt(msg.encode(), self.get_password())

            print(f"{aqua}[{red}${aqua}] {red}Encrypted MSG{aqua}:{red} {encrypted_msg.decode()}")

            
        elif not encryption:
            
            try:
                decrypted_msg = self.e_obj.fernet_decrypt(msg.encode(),self.get_password(False))

                print(f"{aqua}[{red}${aqua}] {red}Decrypted MSG{aqua}:{red} {decrypted_msg.decode()}")

            except Exception as e:

                print(e)

                print(f"{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!")
                exit(1)


    def aes_file_action(self, path, encryption=True):

        self.check_dir(path)

        self.check_file(path)
            
        if encryption:

            encrypted_file = self.f_obj.fernet_encrypt_file(path, self.get_password())
            print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!")



        elif not encryption:
            
            try:
                decrypted_file = self.f_obj.fernet_decrypt_file(path, self.get_password(False))

                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!")

            except:
                print(f"\n{aqua}[{red}!{aqua}] {red}Password is incorrect{aqua}!")
                exit(1)



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
            



    def rsa_file_action(self, path, encryption=True):

        self.check_dir(path)

        self.check_file(path)

        if encryption:

            encrypted_file = self.f_obj.rsa_encrypt_file(path)
            print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!")



        elif not encryption:
            
            try:
                decrypted_file = self.f_obj.rsa_decrypt_file(path)
                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!")

            except ValueError:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!")
                exit(1)





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


    def rsa_file_action_load(self, path, key_path, encryption=True):

        self.check_dir(path)

        self.check_file(path)

        if encryption:

            encrypted_file = self.f_obj.rsa_encrypt_file_load(path, key_path)
            print(f"{aqua}[{red}${aqua}] {red}{path} Encrypted successfully {aqua}!")

        elif not encryption:
            
            try:
                decrypted_file = self.f_obj.rsa_decrypt_file_load(path, key_path)
                print(f"{aqua}[{red}${aqua}] {red}{path} Decrypted successfully {aqua}!")

            except:

                print(f"{aqua}[{red}!{aqua}] {red}Wrong Decryption Key {aqua}!")
                exit(1)
