#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def vowel_words():
    with open('text.txt') as f:
        words = f.read().splitlines()
        vowels = ('a', 'e', 'y', 'u', 'i', 'o')
        v = []
        for word in words:
            if word.lower().startswith(vowels):
                v.append(word)
        print(v)


if __name__ == "__main__":
    vowel_words()
