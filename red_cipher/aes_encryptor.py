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

        # get the encrypted extention from the json file !
        self.ext = self.h_obj.getExt()

        self.iv = secrets.token_bytes(self.iv_length)



    # Simple function for generating random 256 bit key and encode it
    def generateKey(self, enc="base64"):

        if enc.lower() == "base64":

            return b64encode(secrets.token_bytes(self.key_length))

        elif enc.lower() == "hex":

            return hexlify(secrets.token_bytes(self.key_length))

        # if the arg sommethig else we will retrun
        # key as byte formated
        else: return secrets.token_bytes(self.key_length)


    # this function convert plaintext to SHA-256 hashed text ( 32 bytes )
    def password2AesKey(self, password):

        # check if the user want to use salt
        if self.h_obj.getUseSalt() == True:

            return hashlib.sha256(self.saltPassword(password).encode()).digest()

        else:
            return hashlib.sha256(password.encode()).digest()

    
    # simple function for salting passwords !
    def saltPassword(self, password):

        # get the salt from settings file
        salt = self.h_obj.getSalt()

        # devide the length of the salt by 2 to get the middle
        mid_salt = len(salt) // 2

        # check if length of salt is even !
        if (len(salt) % 2) == 0:

            return salt[:mid_salt] + password + salt[mid_salt:]

        # odd length
        else:

            return password + salt




    # simple function to shred data and delete it 4Ever !
    def shredingData(self, path, passes=3):
        
        # open the file and overwrite encrypted data with random data
        with open(path, "br+") as delfile:

            fileSize = delfile.tell()

            for _ in range(passes):

                # return to the begin of the file
                delfile.seek(0)
                
                # write to the file random data
                delfile.write(secrets.token_bytes(fileSize))

            delfile.seek(0)

            # write zeros to the file
            delfile.write(b"\0" * fileSize)

        # finally delete the file
        os.remove(path)
        



    # Encrypt function with AES-256 CBC mode !
    def aesEncrypt(self, data, key):

        # initialize AES cipher object
        cipher = AES.new(key, AES.MODE_CBC, self.iv)

        # encrypt and pad the data with size of block (16)
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))

        # combine IV with encrpted data
        return self.iv + encrypted_data


    # Decrypt function with AES-256 CBC mode !
    def aesDecrypt(self, enc_data, key):
        
        # extract frist 16 byte (IV)
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


        file.close()

        if enc_filename != False:

            with open(enc_filename, "wb") as enc_file:

                encrypted_data = self.aesEncrypt(data, key)

                enc_file.write(encrypted_data)


            enc_file.close()

        else:

            with open(filename + self.ext, "wb") as enc_file:

                encrypted_data = self.aesEncrypt(data, key)

                enc_file.write(encrypted_data)


            enc_file.close()


        self.shredingData(filename)


    # Decrypt file with AES-256 CBC mode !
    def aesDecryptFile(self, enc_filename, key):

        dec_filename = self.encryptFileName(enc_filename, key, False)


        
        with open(enc_filename, "rb") as enc_file:

            enc_data = enc_file.read()

        enc_file.close()

        if dec_filename != False:

            with open(dec_filename, "wb") as dec_file:

                decrypted_data = self.aesDecrypt(enc_data, key)

                dec_file.write(decrypted_data)


            dec_file.close()

        else:

            # split path to get filename !
            filename = os.path.splitext(enc_filename)

            with open(filename[0], "wb") as dec_file:

                decrypted_data = self.aesDecrypt(enc_data, key)

                dec_file.write(decrypted_data)

            dec_file.close()

        self.shredingData(enc_filename)


    # simple function take a path extract filename
    # and return it encrypted / decrypted !
    def encryptFileName(self, filepath, key, encryption=True):

        dirname = os.path.dirname(filepath)
        basename = os.path.basename(filepath)

        if filepath in os.listdir("."):
            dirname = "." + dirname
        

        if self.h_obj.getEncryptFileName() == True:

            if encryption:

                return str(Path(dirname + "/" + hexlify(self.aesEncrypt(basename.encode(), key)).decode() + self.ext))

            elif not encryption:

                return str(Path(dirname + "/" + self.aesDecrypt(unhexlify(basename.replace(self.ext, "").encode()), key).decode()))

        else: return False
