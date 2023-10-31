#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0:
            print("0{:1d}, ".format(j), end="" if j != 9 else "\n")
        else:
            print("{:02d}, ".format(i * 10 + j), end="" if i != 8 or j != 9 else "\n")
