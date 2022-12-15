from re import findall
from sys import stdin

# Part 2
(n:=map(int,findall('-?\d+',stdin.read()))) and (s:=[(a,b,abs(a-c)+abs(b-d)) for a,b,c,d in zip(n,n,n,n)]) and print(next(x*4000000+y for u,v,w in s for a in [-1,1] for b in [-1,1] for k in range(w+2) for x,y in [(u+a*k,v+b*(w+1-k))] if 0<=x<=4000000 and 0<=y<=4000000 and all(abs(x-t[0])+abs(y-t[1])>t[2] for t in s)))
