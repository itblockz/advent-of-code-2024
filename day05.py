def test(rules, A):
    for i in range(len(A)):
        for j in range(i):
            if f"{A[i]}|{A[j]}" in rules:
                return False
            
        for j in range(i+1, len(A)):
            if f"{A[j]}|{A[i]}" in rules:
                return False
            
    return True

def part1():
    f = open("input.txt")
    rules = set()
    first_sec = True
    ans = 0
    for x in f:
        if x == '\n':
            first_sec = False
            continue
        
        if first_sec:
            rules.add(x.removesuffix('\n'))
        else:
            A = list(map(int, x.split(",")))
            if test(rules, A):
                ans += A[len(A) // 2]
                        
    print(ans)

def sort(rules, A):
    B = []
    for a in A:
        for i in range(len(B) + 1):
            if i == len(B) or not f"{B[i]}|{a}" in rules:
                B.insert(i, a)
                break
                
    return B

def part2():
    f = open("input.txt")
    rules = set()
    first_sec = True
    ans = 0
    for x in f:
        if x == '\n':
            first_sec = False
            continue
        
        if first_sec:
            rules.add(x.removesuffix('\n'))
        else:
            A = list(map(int, x.split(",")))
            if not test(rules, A):
                A = sort(rules, A)
                ans += A[len(A) // 2]
                        
    print(ans)

part2()