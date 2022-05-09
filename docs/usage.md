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