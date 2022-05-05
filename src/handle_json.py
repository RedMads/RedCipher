import json
import os
from pathlib import Path

class HandleJson:

    def __init__(self):

        self.settings = {}

        # get the settings filepath 
        self.settingsPath =  os.path.join(os.path.dirname(__file__)[:-4], "settings.json")
    
    # This function load the settings file !
    def loadJson(self):

        try:

            # Try to read the < settings.json > file !
            with open(self.settingsPath, "r") as json_file:

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


    def getExt(self):

        return self.settings["settings"]["extension"]

    def getKeySize(self):

        return self.settings["settings"]["keySize"]

    def getSalt(self):

        return self.settings["settings"]["salt"]

    def getUseSalt(self):
        
        return self.settings["settings"]["useSalt"]

    def getEncryptFileName(self):

        return self.settings["settings"]["encryptFileName"]



if __name__ == '__main__':

    h_obj = HandleJson()

    h_obj.loadJson()

    # test lines 
    print(f"Salt: {h_obj.getSalt()}")
    print(f"Extension: {h_obj.getExt()}")
    print(f"KeySize: {h_obj.getKeySize()}")
