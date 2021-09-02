import json
import os

class Handle_json:

    def __init__(self):

        self.settings = {}

        self.settings_path = os.path.dirname(__file__).replace("/src","") + "/settings.json"

    
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

                    "separator": "#####",
                    "extention": ".redc",
                    "key_size": 2048,
                    "salt": "s%piyAc7MhDN*qAS)}YrrXb.A9_&t!",
                    "use_salt": True
                }
            }

    
    def get_separator(self):

        return self.settings["settings"]["separator"]

    def get_ext(self):

        return self.settings["settings"]["extention"]

    def get_keysize(self):

        return self.settings["settings"]["key_size"]

    def get_salt(self):

        return self.settings["settings"]["salt"]



if __name__ == '__main__':

    h_obj = Handle_json()

    print(f"Salt: {h_obj.get_salt()}")
    print(f"Separator: {h_obj.get_separator()}")
    print(f"Extention: {h_obj.get_ext()}")
    
