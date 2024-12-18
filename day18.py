def dfs_with_stack(A, start_x, start_y, w, h):
    stack = [(start_x, start_y, 0)]
    min_cost = float('inf')
    mem = {}

    while stack:
        items = stack.pop()
        if len(items) == 2:
            x, y = items
            A[y][x] = '.'
            continue
        
        x, y, cost = items
        
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        
        if mem.get((x, y), float('inf')) <= cost:
            continue
        else:
            mem[(x, y)] = cost

        if A[y][x] == '#' or A[y][x] == 'o':
            continue
        
        if x == w - 1 and y == h - 1:
            min_cost = min(min_cost, cost)
            continue

        A[y][x] = 'o'

        stack.append((x, y))
        stack.append((x - 1, y, cost + 1))
        stack.append((x + 1, y, cost + 1))
        stack.append((x, y - 1, cost + 1))
        stack.append((x, y + 1, cost + 1))

    return min_cost

def part1():
    w, h = 71, 71
    n = 1024
    A = [['.'] * w for _ in range(h)]
    f = open('input.txt')
    for _ in range(n):
        x, y = map(int, f.readline().split(','))
        A[y][x] = '#'
        
    ans = dfs_with_stack(A, 0, 0, w, h)
    print(ans)
    
def part2():
    w, h = 71, 71
    
    pos = []
    for line in open('input.txt'):
        pos.append(line.strip())
    
    l = 1024
    r = len(pos)
        
    while l + 1 < r:
        A = [['.'] * w for _ in range(h)]
        m = (l + r) // 2
        
        for i in range(m):
            x, y = map(int, pos[i].split(','))
            A[y][x] = '#'
            
        ans = dfs_with_stack(A, 0, 0, w, h)
        if ans == float('inf'):
            r = m - 1
        else:
            l = m
            
    print(pos[r])
    
part2()