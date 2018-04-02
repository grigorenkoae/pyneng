#!/usr/bin/env python

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']


def find_index(elm,lst):
    index = len(lst) - 1 - lst[::-1].index(elm)
    return index


number = int(input('Please enter a number:'))
print(find_index(number,num_list))

word = input('Please enter a word:')
print(find_index(word,word_list))
