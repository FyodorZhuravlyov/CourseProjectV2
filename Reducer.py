#!/usr/bin/env python

import sys

row_a = 2
col_a = 5
col_b = 3
# необходимо изменить mapper чтобы он создавал подходящие для сортировки значения
num = list()
# for line in open("mapperOutput.txt"):
for line in sys.stdin:
    curr_index, index, value = line.strip().split(" ")
    index, value = map(int, [index, value])
    num.append((curr_index, index, value))
initSum = list()
for i in num:
    checker = 0
    for j in num:
        if i == j:
            if checker == 0:
                checker += 1
                continue
        if i[0] == j[0]:
            if i[1] == j[1]:
                initSum.append([i[0], str(i[1]), ((i[2] % 97) * (j[2] % 97)) % 97])

Out = dict()
counter = 0

for i in initSum:

    tempList = list()
    if i[0] in Out.keys():
        counter += 1
        continue
    counter += 1
    Out[i[0]] = i[2]
    inercounter = 0
    for j in initSum:
        if i[0] == j[0]:
            if i[1] != j[1]:
                inercounter += 1
                if inercounter > col_a - 1:
                    continue
                if j == tempList:
                    inercounter -= 1
                    continue
                Out[i[0]] = ((Out[i[0]] % 97) + (j[2] % 97)) % 97
                tempList = j

# mapperOutputfin = open("mapperOutputfin.txt", "w")

for key, value in Out.items():
    print(key, value)
    # mapperOutputfin.write("%s\t%s" % (key, str(value)) + "\n")
