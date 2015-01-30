#!/usr/bin/env python
# *-* encoding: utf-8 *-*

def find(dat):
    sum = 0
    for i in range(3,dat):
        if i % 3 == 0 or i % 5 == 0 :
            sum = sum + i
    return sum

if __name__ == "__main__":
    print(find(1000))

