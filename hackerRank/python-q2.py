#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 == 1 or (n % 2 == 0 and n in range(6, 21)):
        print("Weird") 
    else:  
        print("Not Weird")    

        
# Q: what is .strip()?  input strip out text format?  
# A: Removes any leading and trailing white spaces.  In case input has white spaces.  
# If .strip(chars) parameter specified, it will strip leading and trailing matching characters.  

# Q why funciton called "if __name__ = '__main__': ?  Why dunders? 

