from itertools import accumulate
from sys import stdin

print(len(set(map(lambda t:t[-1],accumulate((l[0] for l in stdin.readlines() for _ in range(int(l[2:]))),lambda t,p:[*accumulate(t[1:],lambda a,b:((d:=a-b),b+(abs(d)>=2)*((d.real>0)-(d.real<0)+1j*((d.imag>0)-(d.imag<0))))[1],initial=t[0]+{'R':1,'L':-1,'U':1j,'D':-1j}[p])],initial=[0]*10)))))
