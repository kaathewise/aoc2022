from itertools import accumulate
from sys import stdin

# Part 2
print(*('\n'[i%40:]+'.#'[-2<i%40-r<2] for i,r in enumerate(accumulate(stdin.read().split(),lambda r,c:r+(not c.isalpha() and int(c)),initial=1))))
