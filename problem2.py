#!/usr/bin/env python
# *-* encoding: utf-8 *-*

sum = 2
a = 1
b = 2
c = a+b
while c < 4000000 :
    if c % 2 == 0:
        sum = sum + c
    a,b = b,c
    c = a+b

print(sum)

