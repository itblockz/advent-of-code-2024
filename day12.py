def area(A, i, j, label):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
        return 0
    
    if A[i][j] == label:
        A[i][j] = '.' # mark as visited
        return 1 + area(A, i, j - 1, label) + area(A, i - 1, j, label) + area(A, i, j + 1, label) + area(A, i + 1, j, label)
    
    return 0

def perimeter(A, i, j, label):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
        return 1
    
    if A[i][j].islower():
        if A[i][j] == label.lower():
            return 0
        return 1
    
    if A[i][j] != label:
        return 1
    
    A[i][j] = A[i][j].lower() # mark as visited
    
    return perimeter(A, i, j - 1, label) + perimeter(A, i - 1, j, label) + perimeter(A, i, j + 1, label) + perimeter(A, i + 1, j, label)

def part1():
    A = [list(line.strip()) for line in open("input.txt")]
    ans = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j].isupper():
                p = perimeter(A, i, j, A[i][j])
                a = area(A, i, j, A[i][j])
                ans += a * p
    
    print(ans)

def area2(A, B, i, j, label):
    if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
        return 0
    
    if A[i][j] == label:
        A[i][j] = '.'
        B[i][j] = '#' # mark as interest region
        return 1 + area2(A, B, i, j - 1, label) + area2(A, B, i - 1, j, label) + area2(A, B, i, j + 1, label) + area2(A, B, i + 1, j, label)
    
    return 0

def sides(A):
    res = 0
    for i in range(len(A)):
        # top line
        j = 0
        while j < len(A[0]):
            # find top line
            while j < len(A[0]) and not (A[i][j] == '#' and (i == 0 or A[i - 1][j] != '#')):
                j += 1

            if j >= len(A[0]):
                break
            
            # track top line
            while j < len(A[0]) and A[i][j] == '#' and (i == 0 or A[i - 1][j] != '#'):
                j += 1
                
            res += 1
        
        # bottom line
        j = 0
        while j < len(A[0]):
            # find bottom line
            while j < len(A[0]) and not (A[i][j] == '#' and (i == len(A) - 1 or A[i + 1][j] != '#')):
                j += 1

            if j >= len(A[0]):
                break
            
            # track bottom line
            while j < len(A[0]) and A[i][j] == '#' and (i == len(A) - 1 or A[i + 1][j] != '#'):
                j += 1
                
            res += 1
    
    for j in range(len(A[0])):
        # left line
        i = 0
        while i < len(A):
            # find left line
            while i < len(A) and not (A[i][j] == '#' and (j == 0 or A[i][j - 1] != '#')):
                i += 1

            if i >= len(A):
                break
            
            # track left line
            while i < len(A) and A[i][j] == '#' and (j == 0 or A[i][j - 1] != '#'):
                i += 1
                
            res += 1
        
        # right line
        i = 0
        while i < len(A):
            # find right line
            while i < len(A) and not (A[i][j] == '#' and (j == len(A[0]) - 1 or A[i][j + 1] != '#')):
                i += 1

            if i >= len(A):
                break
            
            # track right line
            while i < len(A) and A[i][j] == '#' and (j == len(A[0]) - 1 or A[i][j + 1] != '#'):
                i += 1
                
            res += 1
    
    return res

def part2():
    A = [list(line.strip()) for line in open("input.txt")]
    ans = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j].isupper():
                B = [a.copy() for a in A]
                a = area2(A, B, i, j, A[i][j])
                s = sides(B)
                ans += a * s
    
    print(ans)

part2()