from re import findall
from sys import stdin

# Part 1
#print((n:=map(int,findall(r'\d+',stdin.read()))) and sum((a==c) or (b==d) or (a<c)==(b>d) for (a,b,c,d) in zip(n,n,n,n)))

# Part 2
print((n:=map(int,findall(r'\d+',stdin.read()))) and sum(max(a,c)<=min(b,d) for a,b,c,d in zip(n,n,n,n)))
