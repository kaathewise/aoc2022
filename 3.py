from sys import stdin

#print(sum((l:=len(s)//2) and (p:=ord((set(s[:l])&set(s[l:])).pop())-96) and p+(p<0)*58  for s in stdin.readlines()))
print((s:=(l.strip() for l in stdin.readlines())) and sum((p:=ord((set(a)&set(b)&set(c)).pop())-96) and p+(p<0)*58  for a,b,c in zip(s,s,s)))
