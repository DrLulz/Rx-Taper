#!/usr/local/bin/python

dose = [1, 2.5, 5, 10, 20, 50]
step = 10
start = 50
score = False
days = 100

def count(n, inc):
    if score: inc = inc/2
    while (True) and (n <= days):
        yield n
        n += inc
        
for n in count(start, step):
    print n