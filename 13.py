from sys import stdin

# Part 1
#(t:=lambda x:isinstance(x,int)) and (cmp:=lambda s,a,b:((a>b)-(a<b) if t(a) else s(s,a,[b])) if t(b) else (s(s,[a],b) if t(a) else next((x for c,d in zip(a,b) if (x:=s(s,c,d))),0) or s(s,len(a),len(b)))) and print(sum([i+1 for i,v in enumerate(cmp(cmp,eval(s[0]),eval(s[1]))<0 for p in stdin.read().split('\n\n') for s in [p.split()]) if v]))

# Part 2
(t:=lambda x:isinstance(x,int)) and (cmp:=lambda s,a,b:((a>b)-(a<b) if t(a) else s(s,a,[b])) if t(b) else (s(s,[a],b) if t(a) else next((x for c,d in zip(a,b) if (x:=s(s,c,d))),0) or s(s,len(a),len(b)))) and (x:=sum((cmp(cmp,eval(s),[[2]])<0)+1j*(cmp(cmp,eval(s),[[6]])<0) for s in stdin.read().split())) and print((x.real+1)*(x.imag+2))
