from collections import Counter
from functools import reduce
from re import findall
from sys import stdin

print((m:=[]) or (c:=Counter()) or reduce(lambda s,c:((*s[:-1],) if c[3]=='.' else (*s,c)) if c[0]=='c' else m.append((s,sum(map(int, findall(r'\d+',c))))) or s,stdin.read().split('$ ')[1:],()) and any(c.update({(*p[0][:i+1],):p[1]}) for p in m for i in range(len(p[0]))) or next(x for x in sorted(c.values()) if x>=c[('cd /\n',)]-40000000))
