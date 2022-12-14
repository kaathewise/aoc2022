from re import findall
from sys import stdin

# Part 2
((i:=stdin.read().split('\n\n')),(m:=[[*filter(str.isalpha,reversed(s))] for c,s in enumerate(zip(*i[0].split('\n'))) if c%4==1]),(t:=map(int,findall(r'\d+',i[1]))),[(m[b-1].extend(m[a-1][-k:]),[m[a-1].pop() for _ in range(k)]) for k,a,b in zip(t,t,t)],print(''.join(x[-1] for x in m)))
