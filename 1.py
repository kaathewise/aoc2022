from sys import stdin

# Part 2
print(sum(sorted([sum(map(int,e.split())) for e in stdin.read().split('\n\n')])[-3:]))
