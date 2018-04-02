#!/usr/bin/env python

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']



number = input('Please enter a number:')

index = len(num_list) - 1 - num_list[::-1].index(int(number))
print(index)


word = input('Please enter a word:')

index = len(word_list) - 1 - word_list[::-1].index(word)
print(index)
