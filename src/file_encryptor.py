from src.encryptor import Encryptor
from src.handle_json import Handle_json
from src.aes_encryptor import AES_encryptor
from os import remove, path



# The Main class !
class FileEncryptor:


    def __init__(self):

        self.e_obj = Encryptor()
        self.h_obj = Handle_json()
        self.a_obj = AES_encryptor()
        
        self.h_obj.load_json()

        self.ext = self.h_obj.get_ext()


    # This Function Encrypt a File with RSA public key !
    # Args < filepath: String > 
    # Return Encrypted File !
    def rsa_encrypt_file(self, filepath):

        with open(filepath, "rb") as file:

            data = file.read()

            key, encrypted_data = self.e_obj.rsa_encrypt(data)

            file.close()

        enc_filename = self.a_obj.ED_filename(filepath, key)

        if enc_filename != False:

            with open(enc_filename, "wb") as enc_file:

                enc_file.write(encrypted_data.encode())

            enc_file.close()

        
        else:

            with open(filepath + self.ext, "wb") as enc_file:

                enc_file.write(encrypted_data.encode())

            enc_file.close()

        self.a_obj.shreding_data(filepath)


            
    # This Function Decrypt a Encrypted File with RSA private key !
    # Args < filepath: String > 
    # Return Decrypted File !   
    def rsa_decrypt_file(self, filepath):

        filename = path.splitext(filepath)

        with open(filepath, "rb") as enc_file:

            encrypted_data = enc_file.read()

            key, decrypted_data = self.e_obj.rsa_decrypt(encrypted_data)

        enc_file.close()

        dec_filename = self.a_obj.ED_filename(filepath, key, False)

        if dec_filename != False:

            with open(dec_filename, "wb") as file:

                file.write(decrypted_data)

            file.close()

        else:

            with open(filename[0], "wb") as file:

                file.write(decrypted_data)

            file.close()

        self.a_obj.shreding_data(filepath)


    # This Function Encrypt a File with loaded RSA public key !
    # Args < filepath: String > & < pub_key_path: string >
    # Return Encrypted File ! 
    def rsa_encrypt_file_load(self, filepath, pub_key_path):

        with open(filepath, "rb") as file:

            data = file.read()

            key, encrypted_data = self.e_obj.rsa_encrypt_load(data, pub_key_path)

            file.close()

        enc_filename = self.a_obj.ED_filename(filepath, key)

        if enc_filename != False:

            with open(enc_filename, "wb") as enc_file:

                enc_file.write(encrypted_data.encode())

            enc_file.close()

        
        else:

            with open(filepath + self.ext, "wb") as enc_file:

                enc_file.write(encrypted_data.encode())

            enc_file.close()

        self.a_obj.shreding_data(filepath)



    # This Function Decrypt a Encrypted File with loaded RSA private key !
    # Args < filepath: String > & < priv_key_path: string >
    # Return Decrypted File ! 
    def rsa_decrypt_file_load(self, filepath, priv_key_path):

        filename = path.splitext(filepath)

        with open(filepath, "rb") as enc_file:

            encrypted_data = enc_file.read()

            key, decrypted_data = self.e_obj.rsa_decrypt_load(encrypted_data, priv_key_path)

        enc_file.close()

        dec_filename = self.a_obj.ED_filename(filepath, key, False)

        if dec_filename != False:

            with open(dec_filename, "wb") as file:

                file.write(decrypted_data)

            file.close()

        else:

            with open(filename[0], "wb") as file:

                file.write(decrypted_data)

            file.close()

        self.a_obj.shreding_data(filepath)

