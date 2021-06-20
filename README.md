# RedCipher
Advanced Encryption / Decryption tool !


# Screenshot
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/help.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/aes_encrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/aes_decrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/rsa_encrypt.png)
![RedCipher](https://github.com/RedMads/RedCipher/blob/main/screenshots/rsa_decrypt.png)

## Usage AES:
***
encrypt Text with AES:
```
python3 red_cipher.py -e aes -m "Your Message"
```
***
decrypt Cipher text with AES:
```
python3 red_cipher.py -d aes -m "Encrypted Messsge"
```
***
encrypt File with AES:
```
python3 red_cipher.py -e aes -f FILENAME
```
***
decrypt encrypted File with AES:
```
python3 red_cipher.py -d aes -f ENC_FILENAME.redc
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
