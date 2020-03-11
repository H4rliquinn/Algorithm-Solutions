"""
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    total=0
    repeats=n//len(s)
    total+=s.count('a')*(repeats)
    total+=s[:n-(len(s)*repeats)].count('a')
    return total

if __name__ == '__main__':
    s='aba'
    n=10
    result = repeatedString(s, n)
    print(result)