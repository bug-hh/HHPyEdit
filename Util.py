#!/usr/bin/env python3

import os

def handle():
    with open("KW.txt", "r") as fobj:
        content = fobj.read()
        ls = content.split("@")
        ls = [r'"\\b@%s\\b", ' % (item.strip()) for item in ls if len(item.strip())]

        for item in ls:
            print(item)

if __name__ == '__main__':
    handle()