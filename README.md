# What is RedCipher ?
a useful program helps you encrypt your sensitive messages or files, with powerful and secure algorthims


# Screenshots
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/help.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/aes_encrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/aes_decrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/rsa_encrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/rsa_decrypt.png)

## Flags:
***
```
usage: red_cipher.py [-h] [-e] [-d] [-f] [-m] [-g] [-l]

optional arguments:
  -h, --help        show this help message and exit
  -e , --encrypt    -e < AES, RSA > : to encrypt
  -d , --decrypt    -d < AES, RSA > : to decrypt
  -f , --file       -f < filePath > : specify file path
  -m , --message    -m < message > : specify message
  -g , --generate   -g < byteSize > : generate rsa keys
  -l , --load       -l < keyFilePath > : load key file to encrypt or decrypt
```

## Usage AES:
***
encrypt message:
```
python3 red_cipher.py -e aes -m "Your Message"
```

decrypt message:
```
python3 red_cipher.py -d aes -m "Encrypted Messsge"
```

encrypt file:
```
python3 red_cipher.py -e aes -f fileName
```

decrypt file:
```
python3 red_cipher.py -d aes -f encFileName.redc
```

## Usage RSA:
***
encrypt message:
```
python3 red_cipher.py -e rsa -m "Your Message"
```
decrypt message:
```
python3 red_cipher.py -d rsa -m "Encrypted Message"
```

encrypt file:
```
python3 red_cipher.py -e rsa -f fileName
```

decrypt file:
```
python3 red_cipher.py -d rsa -f encFileName.redc
```

specify costum key to encrypt or decrypt:
```
python3 red_cipher.py -l keyFileName.pem
```

## Settings:

```json

{
    "settings": {

        "extension": ".redc",
        "keySize": 2048,
        "salt": "s%piyAc7MhDN*qAS)}YrrXb.A9_&t!",
        "useSalt": true,
        "encryptFileName": false
        
    }
}


```
`extension` this object store the encrypted file extension

`keySize` the default size of bits for RSA keys generation

`salt` stores the salt for salting AES key and make it secure ( you can change it ! )

`useSalt` stores boolean value `false` it will not use the salt `true` it will use the salt

`encryptFileName` stores boolean value if `false` it will not encrypt file names for the encrypted files if it `true` it will encrypt it

## install for  linux
***
```
git clone https://github.com/RedMads/RedCipher.git

cd RedCipher

pip3 install -r requirements.txt
```



## install for  Termux
***
```
git clone https://github.com/RedMads/RedCipher.git

cd RedCipher

pip3 install -r requirements.txt 
```



## install for  Windows
make sure python is installed 
***
```
# Download ZipFile, go to click Code -> Download ZIP

# Extract "RedCipher-main.zip"

cd RedCipher

installers/install_windows.bat
```

## special thanks to:
- [Zaky202](https://github.com/Zaky202) - for fixing color issue on windows
- [greedalbadi](https://github.com/greedalbadi) - resort classes and file imports