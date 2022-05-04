import json
import os
from pathlib import Path

class Handle_json:

    def __init__(self):

        self.settings = {}

        # get the settings filepath 
        self.settings_path =  os.path.join(os.path.dirname(__file__)[:-4], "settings.json")
    
    # This function load the settings file !
    def load_json(self):

        try:

            # Try to read the < settings.json > file !
            with open(self.settings_path, "r") as json_file:

                self.settings = json.loads(json_file.read())

            json_file.close()

        except FileNotFoundError:

            # if < settings.json > is missing load the default settings !
            self.settings = {
                "settings": {

                    "extension": ".redc",
                    "keySize": 2048,
                    "salt": "s%piyAc7MhDN*qAS)}YrrXb.A9_&t!",
                    "useSalt": True,
                    "encryptFileName": False

                }
            }


    def get_ext(self):

        return self.settings["settings"]["extension"]

    def get_keysize(self):

        return self.settings["settings"]["keySize"]

    def get_salt(self):

        return self.settings["settings"]["salt"]

    def getUseSalt(self):
        
        return self.settings["settings"]["useSalt"]

    def getEncryptFileName(self):

        return self.settings["settings"]["encryptFileName"]



if __name__ == '__main__':

    h_obj = Handle_json()

    h_obj.load_json()

    # test lines 
    print(f"Salt: {h_obj.get_salt()}")
    print(f"Extension: {h_obj.get_ext()}")
    print(f"KeySize: {h_obj.get_keysize()}")
