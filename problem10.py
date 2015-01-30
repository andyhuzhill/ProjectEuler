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
for i in xrange(0, 2000000):
    prime.append(i)

for i in xrange(2, 2000000):
    n = 2
    while i*n < 2000000:
        prime[i*n] = 0
        n += 1

sum = 0
for i in xrange(2, len(prime)):
    sum += prime[i]

print "sum={0}".format(sum)

