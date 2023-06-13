#!/usr/bin/env python3

import red_cipher as rc


if __name__ == "__main__":
    json = rc.HandleJson()
    json.loadJson()

    print(json.getVal("encryptFileName"))
