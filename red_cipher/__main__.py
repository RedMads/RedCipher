from .actions import Action
from .banner import *
from .handle_json import HandleJson
from .rsa_encryptor import RsaEncryptor
import argparse, platform, logging, coloredlogs
import os


class Main:


    def __init__(self):

        self.e_obj = RsaEncryptor()
        self.a_obj = Action()
        self.h_obj = HandleJson()

        self.h_obj.loadJson()

        self.keySize = self.h_obj.getKeySize()

        self.programPath = os.path.join(os.path.expanduser("~"), ".RedCipher/")

        self.mode = ["encryption", "decryption"]
        self.algrothims = ["rsa","aes"]

        self.enc_mode = None
        self.msg = ""
        self.algo = None
        self.file_mode = False
        self.file_path = None
        self.load_mode = False
        self.load_path = ""
        
        self.show_help = True
        self.help = None
        

    def check_args(self):

        parser = argparse.ArgumentParser()
        
        
        parser.add_argument("-e", "--encrypt", required=False, type=str, metavar="", help="-e < AES, RSA > : to encrypt")
        parser.add_argument("-d", "--decrypt", required=False, type=str, metavar="", help="-d < AES, RSA > : to decrypt")
        parser.add_argument("-f","--file", required=False, type= str, metavar="", help="-f < filePath > : specify file path")
        parser.add_argument("-m", "--message", required=False, type=str, metavar="", help="-m < message > : specify message")
        parser.add_argument("-g", "--generate", required=False, type=int, metavar="", help="-g < byteSize > : generate rsa keys")
        parser.add_argument("-l", "--load", required=False, type=str, metavar="", help="-l < keyFilePath > : load key file to encrypt or decrypt")
        

        args = parser.parse_args()


        if args.encrypt:

            self.enc_mode = True
            self.algo = args.encrypt
            self.show_help = False
            

            if str(self.algo).lower() in self.algrothims:
                
                pass

            else:
                parser.print_help()

            
        elif args.decrypt:

            self.enc_mode = False
            self.algo = args.decrypt
            self.show_help = False
 

            if str(self.algo).lower() in self.algrothims:

                pass

            else:

                parser.print_help()


        if args.message:

            self.msg = args.message
            self.show_help = False
 

        elif args.file:

            self.file_mode = True
            self.file_path = args.file
            self.show_help = False
 
        if args.generate:

            self.show_help = False
            self.a_obj.rsaKeyMinAction(args.generate)
            self.a_obj.overwriteKeysAction(args.generate)



        if args.load:

            self.load_mode = True
            self.load_path = args.load
            self.show_help = False

            if self.load_path != "":
                self.a_obj.checkFile(self.load_path, "Key file not found")

        if self.show_help:

            parser.print_help()



    def action(self):
        
        if str(self.algo).lower() == "aes":

            # check if user specify file
            if self.file_mode:

                self.a_obj.aesFileAction(self.file_path, self.enc_mode)

            # user don't specify file
            elif not self.file_mode:

                self.a_obj.aesAction(self.msg, self.enc_mode)


        elif str(self.algo).lower() == "rsa":

            if self.file_mode:
                
                self.a_obj.checkAll(self.file_path)
                self.a_obj.rsaFileAction(self.file_path, self.load_path, self.enc_mode)

            
            else:

                self.a_obj.rsaAction(self.msg, self.load_path, self.enc_mode)



    # function check if main directory of program is exsits or no
    def checkProgramPaths(self):

        if not os.path.exists(self.programPath):
            os.mkdir(self.programPath)

        filesInMainPath = os.listdir(self.programPath)
        
        if "settings.json" not in filesInMainPath:
            self.h_obj.writeSettings()

        if "Keys" not in filesInMainPath:
            os.mkdir(self.e_obj.keys_dir)
            self.e_obj.generateRsaKeys(self.keySize)

        # check if Keys directory is empty then we will generate keys
        if os.listdir(self.e_obj.keys_dir) == []:
            self.e_obj.generateRsaKeys()


def main():

    # Install ColorLogger if the system is windows
    if platform.system().lower() == "windows":
        logger = logging.getLogger(f"Logger")
        coloredlogs.install(logger=logger)

    outputBanner()
    m_obj = Main()
    m_obj.checkProgramPaths()
    m_obj.check_args()
    m_obj.action()

    # Reset Terminal Color
    print(reset)

if __name__ == "__main__":

    main()