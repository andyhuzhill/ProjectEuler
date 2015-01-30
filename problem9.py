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


for a in range(1,1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            if a +b + c == 1000 and a*a+b*b==c*c:
                print a, b, c
