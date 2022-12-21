from fractions import Fraction
from sys import stdin

# Part 1
# (m:={s[:4]:(lambda e:lambda:e if len(e)<9 else '(%s%s%s)'%(m[e[:4]](),e[5],m[e[7:11]]()))(s[6:-1]) for s in stdin.readlines()}) and print(eval(m['root']()))

# Part 2
(m:={s[:4]:(lambda e:lambda:'Fraction(%s)'%e if len(e)<9 else '(%s%s%s)'%(m[e[:4]](),e[5],m[e[7:11]]()))(s[6:-1] if s[:4]!='root' else s[6:11]+'-'+s[12:]) for s in stdin.readlines()}) and (t:=[m.update({'humn':(lambda:x)}) or eval(m['root']()) for x in [0,1]]) and print(t[0]/(t[0]-t[1]))
