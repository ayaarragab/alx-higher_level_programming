with open('.././models/base.py', 'r', encoding='UTF-8') as f:
        firstLine = f.readline()
        TrueOrFalse = firstLine == '#!/usr/bin/python3'
