def part1():
    A = [list(line.strip()) for line in open("input.txt")]
    points_dict = {}
    for i in range(len(A)):
        for j in range(len(A[0])):
            points_dict[A[i][j]] = points_dict.get(A[i][j], []) + [[i, j]]
            
    points_dict.pop('.')
    
    for points in points_dict.values():
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                y1, x1 = points[i]
                y2, x2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if y2 + dy >= 0 and y2 + dy < len(A) and x2 + dx >= 0 and x2 + dx < len(A[0]):
                    A[y2 + dy][x2 + dx] = '#' 
                if y1 - dy >= 0 and y1 - dy < len(A) and x1 - dx >= 0 and x1 - dx < len(A[0]):
                    A[y1 - dy][x1 - dx] = '#' 
                
    ans = 0
    for i in range(len(A)):
        # print(''.join(A[i]))
        for j in range(len(A[0])):
            if A[i][j] == '#':
                ans += 1
                
    print(ans)

def part2():
    A = [list(line.strip()) for line in open("input.txt")]
    points_dict = {}
    for i in range(len(A)):
        for j in range(len(A[0])):
            points_dict[A[i][j]] = points_dict.get(A[i][j], []) + [[i, j]]
            
    points_dict.pop('.')
    
    for points in points_dict.values():
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                y1, x1 = points[i]
                y2, x2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                while y2 >= 0 and y2 < len(A) and x2 >= 0 and x2 < len(A[0]):
                    A[y2][x2] = '#' 
                    x2 += dx
                    y2 += dy
                    
                while y1 >= 0 and y1 < len(A) and x1 >= 0 and x1 < len(A[0]):
                    A[y1][x1] = '#'
                    x1 -= dx
                    y1 -= dy
                
    ans = 0
    for i in range(len(A)):
        # print(''.join(A[i]))
        for j in range(len(A[0])):
            if A[i][j] == '#':
                ans += 1
                
    print(ans)

part2()