from src.encryptor import Encryptor
from os import remove, path
from src.handle_json import Handle_json



# The Main class !
class FileEncryptor:


    def __init__(self):

        self.e_obj = Encryptor()
        self.h_obj = Handle_json()
        
        self.h_obj.load_json()

        self.ext = self.h_obj.get_ext()


    # This Function Encrypt a File with RSA public key !
    # Args < filepath: String > 
    # Return Encrypted File !
    def rsa_encrypt_file(self, filepath):

        with open(filepath, "rb") as file:

            data = file.read()

            encrypted_data = self.e_obj.rsa_encrypt(data)

            file.close()


        with open(filepath + self.ext, "wb") as enc_file:

            enc_file.write(encrypted_data.encode())

            enc_file.close()

            remove(filepath)


            
    # This Function Decrypt a Encrypted File with RSA private key !
    # Args < filepath: String > 
    # Return Decrypted File !   
    def rsa_decrypt_file(self, filepath):

        filename = path.splitext(filepath)

        with open(filepath, "rb") as enc_file:

            encrypted_data = enc_file.read()

            decrypted_data = self.e_obj.rsa_decrypt(encrypted_data)

            enc_file.close()


        with open(filename[0], "wb") as file:

            file.write(decrypted_data)

            file.close()

            remove(filepath)


    # This Function Encrypt a File with loaded RSA public key !
    # Args < filepath: String > & < pub_key_path: string >
    # Return Encrypted File ! 
    def rsa_encrypt_file_load(self, filepath, pub_key_path):

        with open(filepath, "rb") as file:

            data = file.read()

            encrypted_data = self.e_obj.rsa_encrypt_load(data, pub_key_path)

            file.close()


        with open(filepath + self.ext, "wb") as enc_file:

            enc_file.write(encrypted_data.encode())

            enc_file.close()

            remove(filepath)



    # This Function Decrypt a Encrypted File with loaded RSA private key !
    # Args < filepath: String > & < priv_key_path: string >
    # Return Decrypted File ! 
    def rsa_decrypt_file_load(self, filepath, priv_key_path):

        filename = path.splitext(filepath)

        with open(filepath, "rb") as enc_file:

            encrypted_data = enc_file.read()

            decrypted_data = self.e_obj.rsa_decrypt_load(encrypted_data, priv_key_path)

            enc_file.close()


        with open(filename[0], "wb") as file:

            file.write(decrypted_data)

            file.close()

            remove(filepath)

            
# Test the code up !
if __name__ == "__main__":

    path = "file.txt"

    with open(path, "w") as file:

        file.write("Hello this secret file !")

        file.close()


    ef_obj = FileEncryptor()

    key = ef_obj.e_obj.password_to_fernet_key("password123")

    ef_obj.fernet_encrypt_file(path, key)


