## Flags:

```
usage: redc [-h] [-e] [-d] [-f] [-m] [-g] [-l]

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

encrypt message:
```
redc -e aes -m "Your Message"
```

decrypt message:
```
redc -d aes -m "Encrypted Messsge"
```

encrypt file:
```
redc -e aes -f fileName
```

decrypt file:
```
redc -d aes -f encFileName.redc
```

## Usage RSA:

encrypt message:
```
redc -e rsa -m "Your Message"
```
decrypt message:
```
redc -d rsa -m "Encrypted Message"
```

encrypt file:
```
redc -e rsa -f fileName
```

decrypt file:
```
redc -d rsa -f encFileName.redc
```

specify costum key to encrypt or decrypt:
```
redc -l keyFileName.pem
```