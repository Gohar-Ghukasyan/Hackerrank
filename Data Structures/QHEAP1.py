# Enter your code here. Read input from STDIN. Print output to STDOUT

from __future__ import print_function
import heapq

try:
    input = raw_input
except:
    pass

d = {}
h = []
Q = int(input())
for q in range(Q):
    l = [int(x) for x in input().strip().split(' ')]
    (a, b) = (l[0], l[1] if len(l) > 1 else None)
    if a == 1:
        heapq.heappush(h, b)
    elif a == 2:  # mark for deletion
        if b in d:
            d[b] += 1
        else:
            d[b] = 1
    else:
        while True:
            x = h[0]
            if x in d:
                heapq.heappop(h)
                d[x] -= 1
                if d[x] <= 0: del (d[x])
            else:
                break
        print(x)
