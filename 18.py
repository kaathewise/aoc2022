from sys import stdin

# Part 1
# (s:=stdin.readlines()) and (u:={(i,*(c[k]+(i==k)*j for k in (0,1,2))) for l in s for c in [[*map(int,l.split(','))]] for i in (0,1,2) for j in (0,1)}) and print(2*len(u)-6*len(s))

# Part 2
(c:={(*map(int,l.split(',')),) for l in stdin.readlines()}) and (n:=lambda x,y,z:{(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}) and (C:={z for x in c for y in n(*x) for z in [y,*n(*y)]}-c) and (g:=lambda s,v,f:f and s(s,v|f,{y for x in f for y in n(*x)&C-v})+sum(len(n(*x)&c) for x in f) or 0) and print(g(g,set(),{min(C)}))
