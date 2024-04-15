#!/usr/bin/python3
import os, time

global decoded
while 1:
    decoded = ""
    encodedFile = open("myfile", "rb+")
    i = 0
    last = ""
    encodedBytes = encodedFile.read()

    for byte in encodedBytes:
        if byte > 0 and byte <= 127:
            byte -= 1
        else:
            byte = 10

        if byte != last:
            decoded += chr(byte)
            last = byte
        i += 1

    if len(decoded) > 1:
        print(decoded)
    os.system("echo > myfile")
    time.sleep(1)
