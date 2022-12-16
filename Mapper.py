#!/usr/bin/env python

import sys

row_a = 2
col_a = 5
col_b = 3


# mapperOutput = open("mapperOutput.txt", "w")

# for line in open("Matrix.txt"):

for line in sys.stdin:

    line = line.strip().split(",")
    row = int(line[1])
    col = int(line[2])
    value = int(line[3])

    if line[0] == "A":
        for i in range(col_a):
            key = str(row) + "," + str(i)
            # mapperOutput.write(key + " " + str(col) + " " + str(value) + "\n")
            print(key + " " + str(col) + " " + str(value))
    if line[0] == "B":
        for j in range(row_a):
            key = str(j) + "," + str(col)
            # mapperOutput.write((key + " " + str(row) + " " + str(value)) + "\n")
            print(key + " " + str(row) + " " + str(value))

# mapperOutput.close()
