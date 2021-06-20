
# install some good things !

apt update -y && apt upgrade -y
apt install git python python3 python3-pip rust -y

pkg update -y && pkg upgrade -y
pkg install git python python3 python3-pip rust -y

pip3 install pycryptodome
pip3 install cryptography
pip3 install argparse
