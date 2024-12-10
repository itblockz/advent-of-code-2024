def search(A, cur, i, j):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
        return 0
    
    if str(cur) != A[i][j]:
        return 0
    
    if cur == 9:
        A[i][j] = 'X'
        return 1
    
    return search(A, cur + 1, i - 1, j) + search(A, cur + 1, i + 1, j) + search(A, cur + 1, i, j - 1) + search(A, cur + 1, i, j + 1)

def part1():
    A = [list(line.strip()) for line in open("input.txt")]
    ans = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == '0':
                B = [a.copy() for a in A]
                ans += search(B, 0, i, j)
    
    print(ans)

def search2(A, cur, i, j):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
        return 0
    
    if str(cur) != A[i][j]:
        return 0
    
    if cur == 9:
        return 1
    
    return search2(A, cur + 1, i - 1, j) + search2(A, cur + 1, i + 1, j) + search2(A, cur + 1, i, j - 1) + search2(A, cur + 1, i, j + 1)
    
def part2():
    A = [list(line.strip()) for line in open("input.txt")]
    ans = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == '0':
                B = [a.copy() for a in A]
                ans += search2(B, 0, i, j)
    
    print(ans)
    
part2()