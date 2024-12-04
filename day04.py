def get_str(A, x, y, type, i):
    if x < 0 or x >= len(A[0]) or y < 0 or y >= len(A) or i == 4:
        return ""
    match type:
        case 0:
            return A[y][x] + get_str(A, x, y - 1, type, i + 1)
        case 1:
            return A[y][x] + get_str(A, x + 1, y - 1, type, i + 1)
        case 2:
            return A[y][x] + get_str(A, x + 1, y, type, i + 1)
        case 3:
            return A[y][x] + get_str(A, x + 1, y + 1, type, i + 1)
        case 4:
            return A[y][x] + get_str(A, x, y + 1, type, i + 1)
        case 5:
            return A[y][x] + get_str(A, x - 1, y + 1, type, i + 1)
        case 6:
            return A[y][x] + get_str(A, x - 1, y, type, i + 1)
        case 7:
            return A[y][x] + get_str(A, x - 1, y - 1, type, i + 1)
            

def part1():
    f = open("input.txt")
    A = []
    for x in f:
        x = x.removesuffix('\n')
        A.append(x)
        
    ans = 0
    for y in range(len(A)):
        for x in range(len(A[0])):
            for i in range(8):
                str = get_str(A, x, y, i, 0)
                if str == "XMAS":
                    ans += 1
            
    print(ans)

def test(A, x, y):
    if A[y][x] != 'A':
        return False
    
    B = ['M', 'M', 'S', 'S']
    C = [A[y - 1][x + 1], A[y + 1][x + 1], A[y + 1][x - 1], A[y - 1][x - 1]]
    C.sort()
    if B != C:
        return False
    
    if A[y + 1][x + 1] == A[y - 1][x - 1]:
        return False
    
    return True

def part2():
    f = open("input.txt")
    A = []
    for x in f:
        x = x.removesuffix('\n')
        A.append(x)
    
    ans = 0
    for y in range(1, len(A) - 1):
        for x in range(1, len(A[0]) - 1):
            ans += 1 if test(A, x, y) else 0
            
    print(ans)

part2()