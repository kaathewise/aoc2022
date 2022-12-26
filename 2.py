from sys import stdin

# Part 1
# print(sum((b-a+4)%3*3+b for r in stdin.readlines() for a,b in [(ord(r[0])-64, ord(r[2])-87)]))

# Part 2
print(sum((a+t+1)%3+1+t*3 for r in stdin.readlines() for a,t in [(ord(r[0])-64, ord(r[2])-88)]))
