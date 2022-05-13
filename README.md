# What is RedCipher ?

command line utility help users encrypt messages or files with simple commands


## Overview:

![RedCipher](https://github.com/RedMads/RedCipher/blob/main/.images/RedCipher.gif)



## Guide:

  - [Usage](docs/usage.md)
  - [Settings](#settings)
  - [Installation](#installation)
  - [Contributors](#special-thanks-to)



## Installation
make sure python is installed on your system
```
pip3 install redcipher
```

## Settings:

settings file are created once the program run for the frist time. 

if the settings file not found the program will load the default settings in `src/handle_json.py` file and rewrite the settings in this path `{user-home}/.RedCipher/settings.json`.

let's say if you have already installed the program and have settings in the path the program will load the settings and won't rewrite it again.

```json

{
    "settings": {

        "extension": ".redc",
        "keySize": 3072,
        "salt": "s%piyAc7MhDN*qAS)}YrrXb.A9_&t!",
        "useSalt": true,
        "encryptFileName": false
        
    }
}


```
- `extension` object store the encrypted file extension

- `keySize` default size of bits for RSA keys generation

- `salt` stores the salt for salting AES key and secure it ( you can change it ! )

- `useSalt` stores boolean value to decide if the program use salt or no
  - `false` tells the program don't use salt
  - `true` use the salt

- `encryptFileName` object store boolean value to decide if program encrypt file name or not
  - `false` will not encrypt file name
  - `true` it will encrypt it


## special thanks to:

- [Zaky202](https://github.com/Zaky202) - for fixing color issue on windows
- [greedalbadi](https://github.com/greedalbadi) - resort classes and file imports