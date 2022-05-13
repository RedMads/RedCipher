from setuptools import setup, find_packages

__name__ = "redcipher"
__version__ = "v1.5"
__author__ = "RedMads"
__author_email__ = "redmads@protonmail.com"
__date__ = "2022-5-12"


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

with open("requirements.txt", "r") as reqFile:

    requirements = []

    for line in reqFile.readlines():
        requirements.append(line[:-1])

readme.close()
reqFile.close()



setup(
    name=__name__,
    version=__version__,
    description='Professional Encryption / Decryption program !',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RedMads/RedCipher/',
    author=__author__,
    author_email=__author_email__,

    project_urls={
      'Source': 'https://github.com/RedMads/RedCipher',
      'Report Bugs': 'https://github.com/RedMads/RedCipher/issues',
      'Download': 'https://pypi.org/project/redcipher/#files',
      'Documentation': 'https://github.com/RedMads/RedCipher/blob/master/README.md'
    },

    license='MIT',

    keywords=[
        "python", "encrypt", "decrypt",
        "cipher", "cryptography", "crypto",
        "AES", "RSA", "decryption", "encryption"
       ],

    packages=find_packages(),

    install_requires=['pycryptodome==3.14.1',
     'colorama==0.4.4', 'cryptography==3.3.2', 'argparse==1.4.0', 'coloredlogs==15.0.1'],

    entry_points={
        'console_scripts': [
                "redc=red_cipher.__main__:main",
        ]
	}
)