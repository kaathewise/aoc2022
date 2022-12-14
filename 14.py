from sys import stdin
from re import findall

# Part 1
#(m:={(x,y) for s in stdin.readlines() for z in [map(int,findall('\d+',s))] for p in [[*zip(z,z)]] for (a,b),(c,d) in zip(p,p[1:]) for x in range(min(a,c),max(a,c)+1) for y in range(min(b,d),max(b,d)+1)}) and (M:=len(m)) and (h:=max(v[1] for v in m)) and (lambda s:s(s,(500,0)))(lambda s,v:v[1]>h or v not in m and (next((r for d in (0,-1,1) if (r:=s(s,(v[0]+d,v[1]+1)))),0) or m.add(v))) and print(len(m)-M)

# Part 2
(m:={(x,y) for s in stdin.readlines() for z in [map(int,findall('\d+',s))] for p in [[*zip(z,z)]] for (a,b),(c,d) in zip(p,p[1:]) for x in range(min(a,c),max(a,c)+1) for y in range(min(b,d),max(b,d)+1)}) and (M:=len(m)) and (h:=max(v[1] for v in m)) and (lambda s:s(s,(500,0)))(lambda s,v:v not in m and v[1]<h+2 and (next((r for d in (0,-1,1) if (r:=s(s,(v[0]+d,v[1]+1)))),0) or m.add(v))) or print(len(m)-M)
