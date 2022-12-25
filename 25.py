from sys import stdin

(n:=lambda x:x and n(x[:-1])*5+('012=-'.find(x[-1])+2)%5-2 or 0) and (s:=lambda x:x and ((q:=(x+2)%5-2),s((x-q)//5)+'012=-'[q])[1] or '') and print(s(sum(n(l[:-1]) for l in stdin.readlines())))
