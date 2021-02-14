""" Problem 2: Given an integer, , perform the following conditional actions:
        If  is odd, print Weird
        If  is even and in the inclusive range of 2 to 5, print Not Weird
        If  is even and in the inclusive range of 6 to 20, print Weird
        If  is even and greater than 20, print Not Weird
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n%2!=0):
        print("Weird")
    else:
        if(2<=n<=5):
            print("Not Weird")
        elif(6<=n<=20):
            print("Weird")
        else:
            print("Not Weird")
