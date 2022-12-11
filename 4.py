from re import findall
from sys import stdin

#print((n:=map(int,findall(r'\d+',stdin.read()))) and sum((a==c) or (b==d) or (a<c)==(b>d) for (a,b,c,d) in zip(n,n,n,n)))
print((n:=map(int,findall(r'\d+',stdin.read()))) and sum(max(a,c)<=min(b,d) for a,b,c,d in zip(n,n,n,n)))
