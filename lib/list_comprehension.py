#!/usr/bin/env python3

def return_evens(num_list):
    evens = [nums for nums in num_list if nums % 2 == 0]
    return evens

def make_exclamation(sentence_list):
    exclaimed = [sentence + "!" for sentence in sentence_list]
    return exclaimed