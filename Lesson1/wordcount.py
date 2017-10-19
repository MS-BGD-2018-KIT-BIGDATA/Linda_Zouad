#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
Created on Mon Sep 18 22:04:22 2017

@author: lindazouad

 
 """
import re
import operator

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.

def file_dict(filename):
    countwords = {}
    file = open(filename)
    for word in file.read().split():
        word=word.lower()
        word = re.sub(r"([?!--.:\[_`])",'', word)
        if word not in countwords:
            countwords[word] = 1
        else:
            countwords[word] = countwords[word] + 1
    return countwords


# Then print_words() and print_top() can just call the utility function.

def print_words(filename):
    countwords = file_dict(filename)
    dict = sorted(countwords.keys())
    for word in dict:
        print(word, countwords[word])

def print_top(filename):
    countwords = file_dict(filename)
    dict = sorted(countwords.items(), key=operator.itemgetter(1),reverse=True)
    print(dict[:20])

print_words('/Users/lindazouad/Downloads/google-python-exercises/basic/alice.txt')
print_top('/Users/lindazouad/Downloads/google-python-exercises/basic/alice.txt')
