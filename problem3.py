#!/usr/bin/env python2
# *-* encoding : utf-8 *-*

# this is john M. Pollard's method to divide prime factors

import time

num = input()
print num,'='

div = 2
start = time.clock()
while div <= num :
    while num % div == 0:
        print '*%d'%div
        num = num / div
    div=div+1

print time.clock()-start

