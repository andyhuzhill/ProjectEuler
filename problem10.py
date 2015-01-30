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

import numpy as np

prime = []
for i in range(0, 2000000):
    prime.append(i)

for i in range(2, 2000000):
    n = 2
    while i*n < 2000000:
        prime[i*n] = 0
        n += 1

for i in range(0, len(prime)):
    print prime[i]

print np.sum(prime)

