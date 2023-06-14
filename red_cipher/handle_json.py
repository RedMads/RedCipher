from .banner import *
from .utils import *
import json
import os


class HandleJson:
    def __init__(self):
        self.settings = {}

        # get the settings filepath 
        self.programPath = os.path.join(os.path.expanduser("~"), ".RedCipher/")
        self.settingsPath =  os.path.join(self.programPath, "settings.json")


    def loadJson(self):
        try:
            with open(self.settingsPath, "r") as json_file:
                self.settings = json.load(json_file)

        except FileNotFoundError:
            self.settings = {
                "settings": {
                    "extension": ".redc",
                    "keySize": 3072,
                    "salt": "s%piyAc7MhDN*qAS)}YrrXb.A9_&t!",
                    "useSalt": True,
                    "encryptFileName": False
                }
            }


    def writeSettings(self):
        self.loadJson()
        with open(self.settingsPath, "w") as settingsFile:
            settingsFile.write(json.dumps(self.settings, indent=4))

    def getSettings(self):
        return self.settings["settings"]

    def getVal(self, key):
        return self.settings["settings"][key]


if __name__ == '__main__':
    h_obj = HandleJson()
    h_obj.loadJson()

    # test lines
    print(f"Salt: {h_obj.getVal('salt')}")
    print(f"Extension: {h_obj.getVal('extension')}")
    print(f"KeySize: {h_obj.getVal('keySize')}")
