def height(A):
    h = [0] * 5
    if A[0][0] == '.': # key
        A.reverse()
    for j in range(len(A[0])):
        for i in range(1, len(A)):
            if A[i][j] == '#':
                h[j] += 1
    return h

def part1():
    f = open('input.txt')
    key = []
    lock = []
    line = f.readline().strip()
    while line:
        A = []
        while line:
            A.append(line)
            line = f.readline().strip()
        if A[0][0] == '.':
            key.append(height(A))
        else:
            lock.append(height(A))
        line = f.readline().strip()
    
    ans = 0
    for l in lock:
        for k in key:
            overlap = False
            for i in range(5):
                if l[i] + k[i] > 5:
                    overlap = True
                    break
            if not overlap:
                ans += 1
                
    print(ans)
    
part1()