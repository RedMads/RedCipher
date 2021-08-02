import json


class Handle_json:

    def __init__(self):

        self.settings = {}

    
    # This function load the settings file !
    def load_json(self, filename):

        try:

            # Try to read the < settings.json > file !
            with open(filename, "r") as json_file:

                self.settings = json.loads(json_file.read())

            json_file.close()

        except FileNotFoundError:

            # if < settings.json > is missing load the default settings !
            self.settings = {
                "settings": {

                    "salt": "Abo_Na9r!L*C3%T1GgZ#KqSDYMzi64hS#ilDMBaN*4C0K98MdV#GXl^HIm!",
                    "separator": "#####",
                    "extention": ".redc",
                    "key_size": 4096
                }
            }


    def get_salt(self):

        return self.settings["settings"]["salt"]

    
    def get_separator(self):

        return self.settings["settings"]["separator"]

    def get_ext(self):

        return self.settings["settings"]["extention"]

    def get_keysize(self):

        return self.settings["settings"]["key_size"]





if __name__ == '__main__':

    h_obj = Handle_json()

    h_obj.load_json("settings.json")

    print(f"Salt: {h_obj.get_salt()}")
    print(f"Separator: {h_obj.get_separator()}")
    print(f"Extention: {h_obj.get_ext()}")
    