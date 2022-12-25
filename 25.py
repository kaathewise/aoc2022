from sys import stdin

(n:=lambda x:x and n(x[:-1])*5+'=-012'.find(x[-1])-2 or 0) and (s:=lambda x:x and s((x+2)//5)+'=-012'[(x+2)%5] or '') and print(s(sum(n(l[:-1]) for l in stdin.readlines())))
