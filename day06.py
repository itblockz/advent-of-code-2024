def search(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == '^':
                return i, j

def part1():
    A = [list(line.strip()) for line in open("input.txt")]
    n, m = len(A), len(A[0])
    y, x = search(A)
    ans = 0
    dx, dy = 0, -1
    while x >= 0 and x < m and y >= 0 and y < n:
        if y + dy < 0 or y + dy >= n or x + dx < 0 or x + dx >= m or A[y + dy][x + dx] != '#':
            A[y][x] = 'X'
            x += dx
            y += dy
        else:
            dx, dy = -dy, dx
            
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'X':
                ans += 1
                
    print(ans)

def end(A, x, y):
    n, m = len(A), len(A[0])
    dx, dy = 0, -1
    for i in range(10000):
        if y < 0 or y >= n or x < 0 or x >= m:
            return True
        if y + dy < 0 or y + dy >= n or x + dx < 0 or x + dx >= m or A[y + dy][x + dx] != '#':
            x += dx
            y += dy
        else:
            dx, dy = -dy, dx
                
    return False

def part2():
    A = [list(line.strip()) for line in open("input.txt")]
    y, x = search(A)
    ans = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if y == i and x == j:
                continue
            B = [a.copy() for a in A]
            B[i][j] = '#'
            if not end(B, x, y):
                ans += 1
                
    print(ans)
    
part2()