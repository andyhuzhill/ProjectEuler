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



Flag = False

def get():
    global Flag
    n = 2520
    while not Flag:
        for i in range(1, 21):
            if n % i != 0:
                n += 1
                print n
                break
            elif i == 20 and n % i == 0:
                Flag = True
                return n

if __name__ == "__main__":
    res =get()
    print res

