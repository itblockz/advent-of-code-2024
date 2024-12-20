def dfs_with_stack(A, start_x, start_y, cheat_duration):
    stack = [(start_x, start_y, 0, cheat_duration - 1, 0)]
    cnt = [{}, {}, {}]

    while stack:
        items = stack.pop()
        if len(items) == 3:
            x, y, c = items
            A[y][x] = c
            continue
        
        x, y, cost, cheat_step, cheat_state = items
        
        if x < 0 or x >= len(A[0]) or y < 0 or y >= len(A):
            continue
        
        if A[y][x] == 'o':
            continue
        
        if A[y][x] == '#':
            if cheat_state == 0:
                cheat_state = 1
            elif cheat_state == 2:
                continue
            
        if cheat_state == 1:
            cheat_step -= 1
            if cheat_step == 0:
                cheat_state = 2
        
        if A[y][x] == 'E':
            cnt[cheat_state][cost] = cnt[cheat_state].get(cost, 0) + 1
            continue
        
        stack.append((x, y, A[y][x]))
        A[y][x] = 'o'

        stack.append((x - 1, y, cost + 1, cheat_step, cheat_state))
        stack.append((x + 1, y, cost + 1, cheat_step, cheat_state))
        stack.append((x, y - 1, cost + 1, cheat_step, cheat_state))
        stack.append((x, y + 1, cost + 1, cheat_step, cheat_state))

    return cnt

def part1():
    A = [list(line.strip()) for line in open('input.txt')]
    sx, sy = 0, 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'S':
                sx, sy = j, i
                
    cnt = dfs_with_stack(A, sx, sy, 2)
    no_cheat = cnt[0].popitem()[0]
    ans = sum(map(lambda x:x[1], filter(lambda x:no_cheat - x[0] >= 100, cnt[2].items())))
    print(ans)

def dfs_with_stack2(A, start_x, start_y):
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
        
        if x < 0 or x >= len(A[0]) or y < 0 or y >= len(A):
            continue
        
        if A[y][x] == '#' or A[y][x] == 'o':
            continue

        if mem.get((x, y), float('inf')) <= cost:
            continue
        else:
            mem[(x, y)] = cost
        
        if A[y][x] == 'E':
            min_cost = min(min_cost, cost)
            continue

        A[y][x] = 'o'

        stack.append((x, y))
        stack.append((x - 1, y, cost + 1))
        stack.append((x + 1, y, cost + 1))
        stack.append((x, y - 1, cost + 1))
        stack.append((x, y + 1, cost + 1))

    return min_cost, mem

def part2():
    A = [list(line.strip()) for line in open('input.txt')]
    sx, sy = 0, 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'S':
                sx, sy = j, i
                
    _, mem = dfs_with_stack2(A, sx, sy)
    points = mem.keys()
    cnt = {}
    for x1, y1 in points:
        for x2, y2 in points:
            dist = abs(x2 - x1) + abs(y2 - y1)
            if dist <= 20:
                val = mem[(x2, y2)] - (mem[(x1, y1)] + dist)
                cnt[val] = cnt.get(val, 0) + 1
                
    ans = sum(map(lambda x:x[1], filter(lambda x:x[0] >= 100, cnt.items())))
    print(ans)
    
part2()