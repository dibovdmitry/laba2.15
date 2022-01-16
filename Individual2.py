#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    with open('textfile1.txt', 'r') as text, open('textfile2.txt', 'w') as record:
        for idx, line in enumerate(text, start=1):
            record.write('{}: {}'. format(idx, line))
