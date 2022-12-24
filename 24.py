from itertools import accumulate,count
from sys import stdin

# Part 1
# (m:={i+1j*j:[1,1j,-1,-1j,0]['v>^<.'.find(c)] for i,s in enumerate([*stdin.readlines()][1:-1]) for j,c in enumerate(s[1:-2])}) and (N:=max(x.real for x in m)+1) and (M:=max(x.imag for x in m)+1) and (D:=[1,-1,1j,-1j]) and (q:=N+1j*M-1j) and print(next(x[1] for x in accumulate(count(1),lambda f,i:({y for x in f[0] for d in (0,*D) for y in [x+d] if y in m and all(m.get((y-i*e).real%N+(y-i*e).imag%M*1j,0)!=e for e in D) or y in [-1,q]},i),initial=([-1],0)) if q in x[0]))

# Part 2
(m:={i+1j*j:[1,1j,-1,-1j,0]['v>^<.'.find(c)] for i,s in enumerate([*stdin.readlines()][1:-1]) for j,c in enumerate(s[1:-2])}) and (N:=max(x.real for x in m)+1) and (M:=max(x.imag for x in m)+1) and (D:=[1,-1,1j,-1j]) and (q:=N+1j*M-1j) and (z:=[q,-1,q]) and print(next(x[1] for x in accumulate(count(1),lambda f,i:({(y,k+(z[k]==y)) for x,k in f[0] for d in (0,*D) for y in [x+d] if y in m and all(m.get((y-i*e).real%N+(y-i*e).imag%M*1j,0)!=e for e in D) or y in z},i),initial=([(-1,0)],0)) if (q,3) in x[0]))
