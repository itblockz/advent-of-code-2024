A = []
B = []

f = open("input.txt")
for x in f:
    a, b = map(int, x.split())
    A.append(a)
    B.append(b)

def part1():
    A.sort()
    B.sort()

    sum = 0
    for i in range(len(A)):
        sum+=abs(A[i] - B[i])
        
    print(sum)

def part2():
    cnt = {}
    for b in B:
        cnt[b] = cnt.get(b, 0) + 1
        
    sum = 0
    for a in A:
        sum += a * cnt.get(a, 0)
        
    print(sum)

part2()