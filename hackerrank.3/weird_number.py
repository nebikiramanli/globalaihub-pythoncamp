#!/bin/python3
import math
import os
import random
import re
import sys

def check_weird(n):
    if n % 2 == 1:
        return "Weird"
    elif n in range(2, 6):
        return "Not Weird"
    elif n in range(6, 21):
        return "Weird"
    elif n > 20:
        return "Not Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(check_weird(n))
