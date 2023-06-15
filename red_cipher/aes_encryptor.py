from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import hexlify, unhexlify
from base64 import b64encode
from .handle_json import HandleJson
from pathlib import Path
import hashlib
import os
import secrets


class AesEncryptor:
    def __init__(self):
        self.key_length = 32 # 256 bits key length
        self.iv_length = 16 # 128 bits IV length
        
        self.h_obj = HandleJson()
        self.h_obj.loadJson()

        # get the encrypted extention from the json file
        self.ext = self.h_obj.getVal("extension")
        self.iv = secrets.token_bytes(self.iv_length)


    # Simple function for generating random 256 bit key and encode it
    def generateKey(self, enc="base64"):
        if enc.lower() == "base64":
            return b64encode(secrets.token_bytes(self.key_length))

        elif enc.lower() == "hex":
            return hexlify(secrets.token_bytes(self.key_length))

        # if the arg somethig else we will retrun
        # key as byte formated
        else:
            return secrets.token_bytes(self.key_length)


    # this function convert plaintext to SHA-256 hashed text ( 32 bytes )
    def password2AesKey(self, password):
        # check if the user want to use salt
        if self.h_obj.getVal("useSalt"):
            return hashlib.sha256(self.saltPassword(password).encode()).digest()

        return hashlib.sha256(password.encode()).digest()


    def saltPassword(self, password):
        salt = self.h_obj.getVal("salt")
        
        # get the middle
        mid_salt = len(salt) // 2
        if (len(salt) % 2) == 0:
            return salt[:mid_salt] + password + salt[mid_salt:]

        else:
            return password + salt


    def shreddingData(self, path, passes=3):        
        # open the file and overwrite encrypted data with random data
        with open(path, "br+") as delfile:
            fileSize = delfile.tell()
            
            for _ in range(passes):
                delfile.seek(0)
                # write random data
                delfile.write(secrets.token_bytes(fileSize))

            delfile.seek(0)
            delfile.write(b"\0" * fileSize)
        os.remove(path)


    # Encrypt function with AES-256 CBC mode !
    def aesEncrypt(self, data, key):
        cipher = AES.new(key, AES.MODE_CBC, self.iv)
        encrypted_data = cipher.encrypt(pad(data, AES.block_size)) # encrypt and pad the data with size of block (16)
        
        return self.iv + encrypted_data


    # Decrypt function with AES-256 CBC mode !
    def aesDecrypt(self, enc_data, key):
        iv = enc_data[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # skipping frist 16 bye and decrypt the data
        decrypted_data = cipher.decrypt(enc_data[16:])

        # remove the padding zeros and return the data
        return unpad(decrypted_data, AES.block_size)


    # Encrypt file with AES-256 CBC mode
    def aesEncryptFile(self, filename, key):
        enc_filename = self.encryptFileName(filename, key)

        with open(filename, "rb") as file:
            data = file.read()

        if enc_filename:
            with open(enc_filename, "wb") as enc_file:
                encrypted_data = self.aesEncrypt(data, key)
                enc_file.write(encrypted_data)
        else:
            with open(filename + self.ext, "wb") as enc_file:
                encrypted_data = self.aesEncrypt(data, key)
                enc_file.write(encrypted_data)

        self.shreddingData(filename)


    # Decrypt file with AES-256 CBC mode !
    def aesDecryptFile(self, enc_filename, key):
        dec_filename = self.encryptFileName(enc_filename, key, False)

        with open(enc_filename, "rb") as enc_file:
            enc_data = enc_file.read()

        if dec_filename:
            with open(dec_filename, "wb") as dec_file:
                decrypted_data = self.aesDecrypt(enc_data, key)
                dec_file.write(decrypted_data)
        else:
            # split path to get filename
            filename = os.path.splitext(enc_filename)

            with open(filename[0], "wb") as dec_file:
                decrypted_data = self.aesDecrypt(enc_data, key)
                dec_file.write(decrypted_data)

        self.shreddingData(enc_filename)


    # simple function take a path extract filename
    # and return it encrypted / decrypted !
    def encryptFileName(self, filepath, key, encryption=True):
        if not self.h_obj.getVal("encryptFileName"):
            return False

        dirname = os.path.dirname(filepath)
        basename = os.path.basename(filepath)

        if filepath in os.listdir("."):
            dirname = "." + dirname

        if encryption:
            return str(Path(dirname + "/" + hexlify(self.aesEncrypt(basename.encode(), key)).decode() + self.ext))
        else:
            return str(Path(dirname + "/" + self.aesDecrypt(unhexlify(basename.replace(self.ext, "").encode()), key).decode()))
