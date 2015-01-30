#!/usr/bin/env python
# *-* encoding: utf-8 *-*
#
# =============================================
#      author:    Andy Scout
#    homepage:    http://andyhuzhill.github.com
#
# description:
#
# =============================================

prime = []
prime.append(2)

n = 1 
p = 3
while n < 10001: 
    for i in prime:
        if p % i == 0:
            p += 1
            break
        elif i == prime[-1]:
            prime.append(p)
            p += 1
            n += 1
            break
        
for i in prime:
    print i

