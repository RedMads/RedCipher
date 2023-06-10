from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP 
from os import path
from .handle_json import HandleJson
from .aes_encryptor import AesEncryptor

# RSA Encryptor class
class RsaEncryptor:

    def __init__(self):
        self.h_obj = HandleJson()
        self.a_obj = AesEncryptor()

        self.h_obj.loadJson()
        self.ext = self.h_obj.getVal("extension")
        self.keys_size = self.h_obj.getVal("keySize")


        # Path convert paths to system default format
        # path.dirname extract the dirname of a __file__
        # str(self.key_dir) convert the return value to string
        self.keys_dir = path.join(self.h_obj.programPath, "Keys")
        self.public_key_file = path.join(self.keys_dir, "public.pem")
        self.private_key_file = path.join(self.keys_dir, "private.pem")
        

    def checkCustomKey(self, keyPath: str, privKey: bool=False) -> open:
        if keyPath:
            return open(keyPath)
        
        # if the user didn't specify any path we gonna load default key path
        else:
            if privKey:
                return open(self.private_key_file)
            else:
                return open(self.public_key_file)


    # This Function Generate RSA keys and write them in files !
    # Args < KeySize: int / default: 2048 >
    # Notice: the keys size was taken from constructor function up!     ((xP0: what does this mean?))
    def generateRsaKeys(self, cmd=False, size=2048):
        if cmd:
            # take the size of bytes that user has specify
            private = RSA.generate(size)
            with open(self.private_key_file, "wb") as private_file:
                private_file.write(private.export_key())
                        
            with open(self.public_key_file, "wb") as public_file:
                public_file.write(private.publickey().export_key())

        else:
            private = RSA.generate(self.keys_size)
            with open(self.private_key_file, "wb") as private_file:
                private_file.write(private.export_key())

            with open(self.public_key_file, "wb") as public_file:
                public_file.write(private.publickey().export_key())


    def rsaEncrypt(self, message:bytes, pubkPath=""):
        pubFile = self.checkCustomKey(pubkPath).read()

        pubKey = RSA.import_key(pubFile);         
        rsa_cipher = PKCS1_OAEP.new(pubKey)
        aes_key = self.a_obj.generateKey("None")

        encrypted_data = self.a_obj.aesEncrypt(message, aes_key)
        encrypted_aes_key = rsa_cipher.encrypt(aes_key)
        full_encrypted = encrypted_aes_key + encrypted_data

        return aes_key ,full_encrypted


    def rsaDecrypt(self, enc_message:bytes, privkPath=""):
        privFile = self.checkCostumKey(privkPath, True).read()

        key = RSA.import_key(privFile)
        rsa_cipher = PKCS1_OAEP.new(key)

        enc_aes_key = enc_message[:256]
        aes_key = rsa_cipher.decrypt(enc_aes_key)
        dec_data = enc_message[256:]

        return aes_key, self.a_obj.aesDecrypt(dec_data, aes_key)


    def rsaEncryptFile(self, filepath, keyPath:str):
        with open(filepath, "rb") as file:
            data = file.read()
            key, encrypted_data = self.rsaEncrypt(data, keyPath)


        # check if the use specify encrypt file feature or not
        # if it so we will store the encrypted name of file to variable
        # otherwise we will retrun False to this variable
        enc_filename = self.a_obj.encryptFileName(filepath, key)

        if enc_filename:
            with open(enc_filename, "wb") as enc_file:
                enc_file.write(encrypted_data)

        # append extension to the file
        else:
            with open(filepath + self.ext, "wb") as enc_file:
                enc_file.write(encrypted_data)

        # destroy data from the orignal file and delete it
        self.a_obj.shreddingData(filepath)


    def rsaDecryptFile(self, filepath, keyPath:str):
        # seprate the filename and the extesion
        filename = path.splitext(filepath)

        with open(filepath, "rb") as enc_file:
            encrypted_data = enc_file.read()
            key, decrypted_data = self.rsaDecrypt(encrypted_data, keyPath)

        # check if the user specify encrypt file feature or not
        # if it so we will store the decrypted name of file to variable
        # otherwise we will retrun False to this variable
        dec_filename = self.a_obj.encryptFileName(filepath, key, False)

        if dec_filename:
            with open(dec_filename, "wb") as file:
                file.write(decrypted_data)

        else:
            # open the orignal filename
            with open(filename[0], "wb") as file:
                file.write(decrypted_data)

        self.a_obj.shreddingData(filepath)
