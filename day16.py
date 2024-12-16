mem = {}

def dfs_with_stack(A, start_x, start_y, dx, dy):
    stack = [(start_x, start_y, dx, dy, 0)]
    min_cost = float('inf')

    while stack:
        items = stack.pop()
        if len(items) == 2:
            x, y = items
            A[y][x] = '.'
            continue
        
        x, y, dx, dy, cost = items
            
        if mem.get((x, y, dx, dy), float('inf')) <= cost:
            continue
        else:
            mem[(x, y, dx, dy)] = cost

        if A[y][x] == '#' or A[y][x] == 'o':
            continue
        
        if A[y][x] == 'E':
            min_cost = min(min_cost, cost)
            continue

        A[y][x] = 'o'

        stack.append((x, y))
        stack.append((x + dx, y + dy, dx, dy, cost + 1))
        stack.append((x + dy, y - dx, dy, -dx, cost + 1001))
        stack.append((x - dy, y + dx, -dy, dx, cost + 1001))
        stack.append((x - dx, y - dy, -dx, -dy, cost + 2001))

    return min_cost

def part1():
    A = [list(line.strip()) for line in open('input.txt')]
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'S':
                result = dfs_with_stack(A, j, i, 1, 0)
                print(result)
                break
   
def dfs_best_path(A, best, start_x, start_y):
    stack = [
        (start_x, start_y, -1, 0, 0),
        (start_x, start_y, 1, 0, 0),
        (start_x, start_y, 0, -1, 0),
        (start_x, start_y, 0, 1, 0),
    ]
    while stack:
        x, y, dx, dy, cost = stack.pop()
        if (x, y, dx, dy) in mem and mem[(x, y, dx, dy)] + cost == best:
            A[y][x] = 'O'
            stack.append((x - dx, y - dy, dx, dy, cost + 1))
            stack.append((x - dx, y - dy, dy, -dx, cost + 1001))
            stack.append((x - dx, y - dy, -dy, dx, cost + 1001))
            stack.append((x - dx, y - dy, -dx, -dy, cost + 2001))

def part2():
    A = [list(line.strip()) for line in open('input.txt')]
    best = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'S':
                best = dfs_with_stack(A, j, i, 1, 0)
                
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'E':
                dfs_best_path(A, best, j, i)
                break
            
    ans = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'O':
                ans += 1
                
    print(ans)
    
part2()