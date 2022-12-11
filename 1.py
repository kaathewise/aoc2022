from sys import stdin

print(sum(sorted([sum(map(int,e.split())) for e in stdin.read().split('\n\n')])[-3:]))
