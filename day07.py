def search(A, i, res, v):
    if i == len(A):
        return res == v
    
    return search(A, i + 1, res * A[i], v) or search(A, i + 1, res + A[i], v)

def part1():
    ans = 0
    for line in open("input.txt"):
        res, A = line.split(": ")
        res = int(res)
        A = list(map(int, A.split()))
        if search(A, 1, A[0], res):
            ans += res
            
    print(ans)

def search2(A, i, res, v):
    if i == len(A):
        return res == v
    
    return search2(A, i + 1, res * A[i], v) or search2(A, i + 1, res + A[i], v) or search2(A, i + 1, int(str(res) + str(A[i])), v)

def part2():
    ans = 0
    for line in open("input.txt"):
        res, A = line.split(": ")
        res = int(res)
        A = list(map(int, A.split()))
        if search2(A, 1, A[0], res):
            ans += res
            
    print(ans)
    
part2()