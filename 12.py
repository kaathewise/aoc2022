from sys import stdin
from itertools import accumulate

#(m:={i+1j*j:ord(c) for i,l in enumerate(stdin.readlines()) for j,c in enumerate(l.strip())}) and (s:=next(m.update({x:97}) or x for x,h in m.items() if h==83)) and (v:=set()) or print(next(i for i,f in enumerate(accumulate(m,lambda f,_:v.update(f) or {u+d for u in f for d in (1,-1,1j,-1j) if u+d in m and m[u+d]+(m[u+d]==69)*53<m[u]+2 and not u+d in v},initial={s})) for u in f if m[u]==69))

(m:={i+1j*j:ord(c) for i,l in enumerate(stdin.readlines()) for j,c in enumerate(l.strip())}) and (s:=next(m.update({x:122}) or x for x,h in m.items() if h==69)) and (v:=set()) or print(next(i for i,f in enumerate(accumulate(m,lambda f,_:v.update(f) or {u+d for u in f for d in (1,-1,1j,-1j) if u+d in m and m[u+d]+2>m[u] and not u+d in v},initial={s})) for u in f if m[u]==97))

