
# Some Great librarys!!!!!!
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP 
from base64 import b64decode, b64encode, urlsafe_b64encode, urlsafe_b64decode
from getpass import getuser
from os import mkdir, listdir, chdir, getcwd, urandom, path, remove
from pathlib import Path
from src.handle_json import Handle_json
from src.aes_encryptor import AES_encryptor
import hashlib


# The Main class!
class Encryptor:

    def __init__(self):

        self.h_obj = Handle_json()
        self.a_obj = AES_encryptor()

        self.h_obj.load_json()

        self.sep = self.h_obj.get_separator()
        self.keys_size = self.h_obj.get_keysize()


        self.keys_dir = path.dirname(__file__).replace("/src","") + "/Keys"
        self.public_key_file = self.keys_dir + "/public.pem"
        self.private_key_file = self.keys_dir + "/private.pem"

        


    # This Function check the main keys directory !
    def check_dir(self):

        try:

            c =  getcwd()

            chdir(self.keys_dir)

            chdir(c)

        except:

            mkdir(self.keys_dir)
            self.generate_keys()
            

    # This Function check the < private.pem > & < public.pem > keys!
    def check_files(self):

        key_files  = ["public.pem", "private.pem"]

        files = listdir(self.keys_dir)

        if key_files[0] and key_files[1] in files:

            return True

        else:

            return False



    # This Function Generate RSA keys and write them in files !
    # Args < KeySize: int / default: 4096 >
    # Notice: the keys size was taken from constructor function up! 

    def generate_keys(self, cmd=False, size=2048):

        if not cmd:

            private = RSA.generate(self.keys_size)

            with open(self.private_key_file, "wb") as private_file:
                        
                private_file.write(private.export_key())
                        
            with open(self.public_key_file, "wb") as public_file:

                public_file.write(private.publickey().export_key())

        elif cmd:

            private = RSA.generate(size)

            with open(self.private_key_file, "wb") as private_file:
                        
                private_file.write(private.export_key())
                        
            with open(self.public_key_file, "wb") as public_file:

                public_file.write(private.publickey().export_key())



    # This Function Encrypt a string with tha RSA key !
    # Args < message: String >
    # Return Encrypted Message !

    def rsa_encrypt(self, message):

        key = RSA.import_key(open(self.public_key_file).read()); rsa_cipher = PKCS1_OAEP.new(key)

        aes_key = self.a_obj.generate_key("None"); encrypted_data = self.a_obj.encrypt(message, aes_key)

        encrypted_aes_key = rsa_cipher.encrypt(aes_key)

        full_encrypted = b64encode(encrypted_aes_key).decode() + self.sep + b64encode(encrypted_data).decode()

        return aes_key ,full_encrypted



    
    # This Function Decrypt a encrypted string with RSA key !
    # Args < enc_message: String >
    # Return Decrypted Message !

    def rsa_decrypt(self, enc_message):

        key = RSA.import_key(open(self.private_key_file).read()); rsa_cipher = PKCS1_OAEP.new(key)

        enc_aes_key = enc_message.decode().split(self.sep)[0]; aes_key = rsa_cipher.decrypt(b64decode(enc_aes_key))

        dec_data = enc_message.decode().split(self.sep)[1]

        return aes_key, self.a_obj.decrypt(b64decode(dec_data.encode()), aes_key)



    # This Function Encrypt a string with loaded RSA public key !
    # Args < message: String > & < pub_key_path: String > 
    # Return Encrypted Message !
    def rsa_encrypt_load(self, message, pub_key_path):

        key = RSA.import_key(open(pub_key_path).read()); rsa_cipher = PKCS1_OAEP.new(key)

        aes_key = self.a_obj.generate_key("None"); encrypted_data = self.a_obj.encrypt(message, aes_key)

        encrypted_aes_key = rsa_cipher.encrypt(aes_key)

        full_encrypted = b64encode(encrypted_aes_key).decode() + self.sep + b64encode(encrypted_data).decode()

        return aes_key, full_encrypted


    # This Function Decrypt a Encrypted String with loaded RSA private key !
    # Args < enc_message: Bytes > & < priv_key_path: String > 
    # Return Decrypted Message !
    def rsa_decrypt_load(self, enc_message, priv_key_path):

        key = RSA.import_key(open(priv_key_path).read()); rsa_cipher = PKCS1_OAEP.new(key)

        enc_aes_key = enc_message.decode().split(self.sep)[0]; aes_key = rsa_cipher.decrypt(b64decode(enc_aes_key))

        dec_data = enc_message.decode().split(self.sep)[1]

        return aes_key, self.a_obj.decrypt(b64decode(dec_data.encode()), aes_key)
            
