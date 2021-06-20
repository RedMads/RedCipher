# RedCipher
Advanced Encryption / Decryption tool !


# Screenshot
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

-g < BYTES SIZE > generate new keys

## Usage AES:
***
encrypt Text with AES:
```
python3 red_cipher.py -e aes -m "Your Message"
```

decrypt Cipher text with AES:
```
python3 red_cipher.py -d aes -m "Encrypted Messsge"
```

encrypt File with AES:
```
python3 red_cipher.py -e aes -f FILENAME
```

decrypt encrypted File with AES:
```
python3 red_cipher.py -d aes -f ENC_FILENAME.redc
```

## Usage RSA:
***
encrypt Text with RSA:
```
python3 red_cipher.py -e rsa -m "Your Message"
```
decrypt Cipher text with RSA:
```
python3 red_cipher.py -d rsa -m "Encrypted Message"
```

encrypt File with RSA:
```
python3 red_cipher.py -e rsa -f FILENAME
```

decrypt encrypted file with RSA:
```
python3 red_cipher.py -d rsa -f ENC_FILENAME.redc
```

Use -l to specfiy RSA key file:
```
python3 red_cipher.py -l KEY_PATH.pem
```
***

## install for  linux
***
```
git clone https://github.com/RedMads/RedCipher.git

cd RedCipher

bash install.sh
```
***


## install for  Termux
***
```
git clone https://github.com/RedMads/RedCipher.git

cd RedCipher

bash termux_install.sh
```
***
