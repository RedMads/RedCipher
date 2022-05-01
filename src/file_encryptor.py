from src.encryptor import Encryptor
from src.handle_json import Handle_json
from src.aes_encryptor import AES_encryptor
from os import remove, path


# FileEncryptor class
# handle file encryption / decryption
class FileEncryptor:


    def __init__(self):
        
        # initialize some objects from another classes
        self.e_obj = Encryptor()
        self.h_obj = Handle_json()
        self.a_obj = AES_encryptor()
        
        # load the settings file 
        self.h_obj.load_json()

        # get file extension from settings.json file
        self.ext = self.h_obj.get_ext()


    # This Function Encrypt a File with RSA public key !
    # Args < filepath: String > 
    # Return Encrypted File !
    def rsa_encrypt_file(self, filepath, keyPath:str):

        # open the file that user wants encrypt
        with open(filepath, "rb") as file:
            
            # read all data of the file
            data = file.read()

            # encrypt the data with rsa_encrypt function
            # take the AES key and store it into variable
            # as well encrypted data
            key, encrypted_data = self.e_obj.rsa_encrypt(data, keyPath)

            # close the file
            file.close()

        # check if the use specify encrypt file feature or not
        # if it so we will store the encrypted name of file to variable
        # otherwise we will retrun False to this variable 
        enc_filename = self.a_obj.ED_filename(filepath, key)

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
        self.a_obj.shreding_data(filepath)


            
    # This Function Decrypt a Encrypted File with RSA private key !
    # Args < filepath: String > 
    # Return Decrypted File !   
    def rsa_decrypt_file(self, filepath, keyPath:str):
        
        # seprate the filename and the extesion
        filename = path.splitext(filepath)

        # open the encrypted file as read binary mode
        with open(filepath, "rb") as enc_file:

            # extraxt and read the encrypted data
            encrypted_data = enc_file.read()

            # decrypt the data with rsa_decrypt function
            # take the AES key and store it into variable
            # as well decrypted data
            key, decrypted_data = self.e_obj.rsa_decrypt(encrypted_data, keyPath)

        # close the encrypted file
        enc_file.close()

        # check if the user specify encrypt file feature or not
        # if it so we will store the decrypted name of file to variable
        # otherwise we will retrun False to this variable 
        dec_filename = self.a_obj.ED_filename(filepath, key, False)

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

        self.a_obj.shreding_data(filepath)
