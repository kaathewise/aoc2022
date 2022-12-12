from functools import reduce
from operator import mul
from sys import stdin

print((ms:=[(s:=m.split('\n')) and (eval('['+s[1][17:]+']'),s[2][18:],int(s[3][20:]),int(s[4][28:]),int(s[5][29:]),[0]) for m in stdin.read().split('\n\n')]) and (M:=reduce(mul,(m[2] for m in ms))) and any(((w:=eval(m[1])%M),ms[m[4] if w%m[2] else m[3]][0].append(w)) and m[0].pop() and m[5].insert(0,m[5].pop()+1) for _ in range(10000) for m in ms for old in reversed(m[0])) or (x:=[*sorted(m[5][0] for m in ms)]) and x[-2]*x[-1])
