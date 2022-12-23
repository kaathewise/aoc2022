from functools import reduce
from itertools import accumulate,count
from sys import stdin

# Part 1
# (D:=[-1,1,-1j,1j]) and (m:=reduce(lambda m,i:(p:=lambda x:[x,next((x+d for d in D[i%4:]+D[:i%4] if not {x+d,x+d+1j*d,x+d-1j*d}&m),x)][len({x+a+1j*b for a in [0,1,-1] for b in [0,1,-1]}&m)>1]) and {[z,x][any(p(z+d)==z for d in D if z+d in m and z+d!=x)] for x in m for z in [p(x)]},range(10),{i+j*1j for i,s in enumerate(stdin.readlines()) for j,c in enumerate(s) if c=='#'})) and (v:=lambda x:max(x)-min(x)+1) and print(v([x.imag for x in m])*v([x.real for x in m])-len(m))

# Part 2
(D:=[-1,1,-1j,1j]) and (g:=accumulate(count(),lambda m,i:(p:=lambda x:[x,next((x+d for d in D[i%4:]+D[:i%4] if not {x+d,x+d+1j*d,x+d-1j*d}&m[0]),x)][len({x+a+1j*b for a in [0,1,-1] for b in [0,1,-1]}&m[0])>1]) and (n:={[z,x][any(p(z+d)==z for d in D if z+d in m[0] and z+d!=x)] for x in m[0] for z in [p(x)]}) and (n,i,n==m[0]),initial=({i+j*1j for i,s in enumerate(stdin.readlines()) for j,c in enumerate(s) if c=='#'},0,False))) and print(next(x[1] for x in g if x[2])+1)
