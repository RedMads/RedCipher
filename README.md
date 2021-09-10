# What is RedCipher ?
Simple tool help you Encrypt / Decrypt messages & files !\
keep your sensitive data safe and secure with 2 powerful algrothims AES, RSA


# Screenshots
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/help.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/aes_encrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/aes_decrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/rsa_encrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/rsa_decrypt.png)

## Flags:
***
-e < AES, RSA > encrypt

-d < AES, RSA > decrypt

-m < MESSAGE > specfiy message

-f < FILENAME > specfiy File

-l < KEY_PATH > specfiy Key

-g < BYTES SIZE > bits for RSA keys generation


## Usage AES:
***
encrypt Text:
```
python3 red_cipher.py -e aes -m "Your Message"
```

decrypt Cipher text:
```
python3 red_cipher.py -d aes -m "Encrypted Messsge"
```

encrypt File:
```
python3 red_cipher.py -e aes -f FILENAME
```

decrypt encrypted File:
```
python3 red_cipher.py -d aes -f ENC_FILENAME.redc
```

## Usage RSA:
***
encrypt Text:
```
python3 red_cipher.py -e rsa -m "Your Message"
```
decrypt Cipher text:
```
python3 red_cipher.py -d rsa -m "Encrypted Message"
```

encrypt File:
```
python3 red_cipher.py -e rsa -f FILENAME
```

decrypt encrypted file:
```
python3 red_cipher.py -d rsa -f ENC_FILENAME.redc
```

Use -l to specfiy RSA key:
```
python3 red_cipher.py -l KEY_NAME.pem
```


## Settings:

```json

{
    "settings": {

        "separator": "#####",
        "extention": ".redc",
        "key_size": 2048,
        "salt": "s%piyAc7MhDN*qAS)}YrrXb.A9_&t!",
        "use_salt": true,
        "encrypt_filename": false
        
    }
}


```

`separator` stores the value for split aes key and encrypted data in RSA encryption function

`extention` this object store the encrypted file extention

`key_size` the default size of bits for RSA keys generation

`salt` stores the salt for salting AES key and make it secure ( you can change it ! )

`use_salt` stores boolean value `false` it will not use the salt `true` it will use the salt

`encrypt_filename` stores boolean value if `false` it will not encrypt file names for the encrypted files if it `true` it will encrypt it

## install for  linux
***
```
git clone https://github.com/RedMads/RedCipher.git

cd RedCipher

bash installers/install_linux.sh
```



## install for  Termux
***
```
git clone https://github.com/RedMads/RedCipher.git

cd RedCipher

bash installers/install_termux.sh
```

