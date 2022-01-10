#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    with open('text.txt', 'r', encoding='utf-8') as f:
        words = f.read()

        for word in words.split('.'):
            if "aeyuio" in word:
                print(word)

f.close()
