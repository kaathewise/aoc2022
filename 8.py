from functools import reduce
from operator import mul
from sys import stdin

# Part 2
((m:=[[int(c) for c in s[:-1]] for s in stdin.readlines()]),(t:=[*zip(*m)]),print(max(reduce(mul,(next((k+1 for k,x in enumerate(v) if x>=m[i][j]), len(v)) for v in (m[i][j-1::-1],m[i][j+1:],t[j][i-1::-1],t[j][i+1:]))) for i in range(1,98) for j in range(1,98))))
