#!/usr/bin/python3
"""This module contains a script about
log parsing"""


import sys

statusCodeDict = {'200': 0, '301': 0, '400': 0, '401': 0,
                  '403': 0, '404': 0, '405': 0, '500': 0}
totalSize = 0
count = 0
for line in sys.stdin:
    if line:
        lineContent = line.split()
        statusCode = lineContent[-2]
        fileSize = int(lineContent[-1])
        totalSize += fileSize
        if statusCode in statusCodeDict.keys():
            statusCodeDict[statusCode] += 1
        count += 1

        if count == 10:
            print(f"File size: {totalSize}")
            for key in statusCodeDict.keys():
                if statusCodeDict[key] == 0:
                    continue
                print(f'{key}: {statusCodeDict[key]}')
            count = 0

if count > 0:  # This condition for if the input were less than 10
    print(f"File size: {totalSize}")
    for key in statusCodeDict.keys():
        if statusCodeDict[key] == 0:
            continue
        print(f'{key}: {statusCodeDict[key]}')
