from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP 
from os import path
from .handle_json import HandleJson
from .aes_encryptor import AesEncryptor

# RSA Encryptor class
class RsaEncryptor:

    def __init__(self):

        # initialize some objects
        self.h_obj = HandleJson()
        self.a_obj = AesEncryptor()

        # load json file (settings.json)
        self.h_obj.loadJson()

        self.ext = self.h_obj.getExt()

        # get key-size from settings file
        self.keys_size = self.h_obj.getKeySize()


        # Path convert paths to system default format
        # path.dirname extract the dirname of a __file__
        # str(self.key_dir) convert the return value to string
        self.keys_dir = path.join(self.h_obj.programPath, "Keys")
        self.public_key_file = path.join(self.keys_dir, "public.pem")
        self.private_key_file = path.join(self.keys_dir, "private.pem")

        

    # a function to check if user specify coustum key
    def checkCostumKey(self, keyPath:str, privKey:bool=False) -> open:

        # check if the user specify path for key or not
        if keyPath != "":
            return open(keyPath)
        
        # if the user don't specify any path we gonna load default key path
        else:
            # check if key is private key or not then we load the default key
            if privKey: return open(self.private_key_file)

            else: return open(self.public_key_file)



    # This Function Generate RSA keys and write them in files !
    # Args < KeySize: int / default: 2048 >
    # Notice: the keys size was taken from constructor function up! 

    def generateRsaKeys(self, cmd=False, size=2048):

        # check if the user don't use tag -g to generate keys
        if not cmd:

            # generate RSA private key with default size of bytes
            private = RSA.generate(self.keys_size)

            # open private key file and write the private key
            with open(self.private_key_file, "wb") as private_file:
                        
                private_file.write(private.export_key())

            # open public key file and write the public key      
            with open(self.public_key_file, "wb") as public_file:
                
                # extract public key from private key
                # and export it to pem to write it in file
                public_file.write(private.publickey().export_key())

        # if user use the tag -g to generate keys
        elif cmd:

            # we do the same here

            # take the size of bytes that user has specify
            private = RSA.generate(size)

            with open(self.private_key_file, "wb") as private_file:
                        
                private_file.write(private.export_key())
                        
            with open(self.public_key_file, "wb") as public_file:

                public_file.write(private.publickey().export_key())



    # This Function Encrypt a string with tha RSA key !
    # Args < message: String >
    # Return Encrypted Message !

    def rsaEncrypt(self, message:bytes, pubkPath=""):

        pubFile = self.checkCostumKey(pubkPath).read()

        # import the public key to RSA object
        pubKey = RSA.import_key(pubFile); 
        
        # initialize RSA cipher with the pubKey
        rsa_cipher = PKCS1_OAEP.new(pubKey)

        # generate random AES key
        aes_key = self.a_obj.generateKey("None")
        
        # encrypt the message with AES key
        encrypted_data = self.a_obj.aesEncrypt(message, aes_key)

        # encrypt AES key with RSA key
        encrypted_aes_key = rsa_cipher.encrypt(aes_key)

        # combine encrypted AES key with encrypted data
        full_encrypted = encrypted_aes_key + encrypted_data

        # finally return AES key and encrypted data as bytes
        return aes_key ,full_encrypted



    
    # This Function Decrypt a encrypted string with RSA key !
    # Args < enc_message: String >
    # Return Decrypted Message !

    def rsaDecrypt(self, enc_message:bytes, privkPath=""):

        privFile = self.checkCostumKey(privkPath, True).read()

        # import private key to RSA object
        key = RSA.import_key(privFile)
        
        # create RSA cipher with private key
        rsa_cipher = PKCS1_OAEP.new(key)

        # extraxt the frist 256 bits (Encrypted AES key)
        enc_aes_key = enc_message[:256]
        
        # decrypt aes key with RSA private key
        aes_key = rsa_cipher.decrypt(enc_aes_key)

        # skip 256 bit and extraxt the rest (Encrypted data)
        dec_data = enc_message[256:]

        # finally return AES key and decrypted data
        return aes_key, self.a_obj.aesDecrypt(dec_data, aes_key)

   # This Function Encrypt a File with RSA public key !
    # Args < filepath: String > 
    # Return Encrypted File !
    def rsaEncryptFile(self, filepath, keyPath:str):

        # open the file that user wants encrypt
        with open(filepath, "rb") as file:
            
            # read all data of the file
            data = file.read()

            # encrypt the data with rsa_encrypt function
            # take the AES key and store it into variable
            # as well encrypted data
            key, encrypted_data = self.rsaEncrypt(data, keyPath)

            # close the file
            file.close()

        # check if the use specify encrypt file feature or not
        # if it so we will store the encrypted name of file to variable
        # otherwise we will retrun False to this variable 
        enc_filename = self.a_obj.encryptFileName(filepath, key)

        # check if the encrypted file name don't match False
        if enc_filename != False:
            
            # open new file with the encrypted file name
            with open(enc_filename, "wb") as enc_file:
                
                # write encrypted data
                enc_file.write(encrypted_data)

            # close the file
            enc_file.close()

        # the use don't want to encrypt file name
        else:

            # open new file with orignal name and we add
            # the encryption extension to the file
            # example: test.txt
            # will be: test.txt.redc
            with open(filepath + self.ext, "wb") as enc_file:
                
                # write the encrypted data
                enc_file.write(encrypted_data)

            # close the file
            enc_file.close()

        # destroy data from the orignal file and delete it
        self.a_obj.shredingData(filepath)


            
    # This Function Decrypt a Encrypted File with RSA private key !
    # Args < filepath: String > 
    # Return Decrypted File !   
    def rsaDecryptFile(self, filepath, keyPath:str):
        
        # seprate the filename and the extesion
        filename = path.splitext(filepath)

        # open the encrypted file as read binary mode
        with open(filepath, "rb") as enc_file:

            # extraxt and read the encrypted data
            encrypted_data = enc_file.read()

            # decrypt the data with rsa_decrypt function
            # take the AES key and store it into variable
            # as well decrypted data
            key, decrypted_data = self.rsaDecrypt(encrypted_data, keyPath)

        # close the encrypted file
        enc_file.close()

        # check if the user specify encrypt file feature or not
        # if it so we will store the decrypted name of file to variable
        # otherwise we will retrun False to this variable 
        dec_filename = self.a_obj.encryptFileName(filepath, key, False)

        # check if the decrypted file name don't match False
        if dec_filename != False:
            
            # open new file
            with open(dec_filename, "wb") as file:
                
                # write the decrypted data into the file
                file.write(decrypted_data)

            # close the decrypted file
            file.close()

        else:

            # open the orignal filename
            with open(filename[0], "wb") as file:

                file.write(decrypted_data)

            file.close()

        self.a_obj.shredingData(filepath)
