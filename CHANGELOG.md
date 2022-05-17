# RedCipher v1.0.5 (2022-May-13)
## Removed:
- seprator between AES key and message in RSA encryption
- random encryption in shreding data function
- RSA load functions
- unneeded functions

## Fixed:
- reverse RSA key for encryption and decryption
    - encrypt with private key issue
    - decrypt with public key issue
- order of function calls in check_all() function

## Features:
- windows support
- commnented code
- less lines of code
- keys and settings files are generated inside folder `.RedCipher/` in user home directory
- the project become library now hosted on [pypi](https://pypi.org/project/redcipher/)

<br/>
<br/>
<br/>

# RedCipher v1.0.4 (2021-Sep-10)
## Features:
- Encrypt file name
- Command `-g` back !
- Salting password for more security

## Fixed:
- File permission error

## Added:
we add some objects `settings.json` file
- `salt` object store the salt (you can change it) !
- `use_salt` object is boolean `false` will not use salt `true` it will use salt
- `encrypt_filename` is boolean `false` will not encrypt file name `true `will encrypt file name

<br/>
<br/>
<br/>

# RedCipher v1.0.3 (2021-Aug-21)
## Features
- Shred the original file after encryption
- The encrypted file has less space than before

## Changes
- Replace Cryptography module with Pycryptodome
- Change object `key_size` value to `2048` in `settings.json`

## Removed
- `-g` command was removed temporary
- Remove `salt` object form `settings.json`

<br/>
<br/>
<br/>

# RedCipher v1.0.2 (2021-Aug-10)
## Fixed
- Fix execute the program from other directory BUG
  
## Added
- Add overwrite question to the user !
- Check if the password is empty string and print error message to the user

<br/>
<br/>
<br/>

# RedCipher v1.0.1 (2021-Aug-03)
## Fixed
- Windows subsystem issue

<br/>
<br/>
<br/>


# RedCipher v1.0.0 (2021-Aug-02)

- First release of RedCipher project