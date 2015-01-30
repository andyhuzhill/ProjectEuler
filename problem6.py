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

sum1 = sum2 = 0
for i in range(1, 101):
    sum1 += i**2
    sum2 += i

print sum2**2 - sum1
