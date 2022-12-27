from functools import reduce
from itertools import accumulate,count,cycle
from operator import and_
from sys import stdin

# Part 1
(R:=[x.to_bytes(4,byteorder='little') for x in (0x1e,0x81C08,0x4041C,0x10101010,0x1818)]) and (W:=cycle(enumerate(stdin.read().strip()))) and (t:=[]) or (c:=lambda h,r:h<0 or any(map(and_,r,t[h:]))) and (w:=lambda r,d:any(x&(63*d+1) for x in r) and r or [x<<1 if d else x>>1 for x in r]) and all(t.extend([0]*7) or (lambda _,x,h:any(t.insert(h+i,t.pop(h+i)|x[i]) for i in range(4)) or any(t[-1] or t.pop() for _ in count()))(*next(filter(lambda x:x[0],accumulate(zip(W,range(len(t)-4,-1,-1)),lambda r,q:(t:=w(r[1],q[0][1]=='<')) and (n:=c(q[1],t) and r[1] or t) and (c(q[1]-1,n),n,q[1]),initial=(0,R[i%5]))))) for i in range(2022)) and print(len(t))

