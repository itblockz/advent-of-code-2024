def diff(dir):
    dx = dy = 0
    match dir:
        case '^':
            dy = -1
        case 'v':
            dy = 1
        case '<':
            dx = -1
        case '>':
            dx = 1
    
    return dx, dy

def move(map, dir, cur):
    x, y = cur
    dx, dy = diff(dir)
            
    if map[y + dy][x + dx] == '.':
        map[y][x] = '.'
        map[y + dy][x + dx] = '@'
        cur[0] = x + dx
        cur[1] = y + dy
    elif map[y + dy][x + dx] == 'O':
        k = 2
        while map[y + k*dy][x + k*dx] == 'O':
            k += 1

        if map[y + k*dy][x + k*dx] == '.':
            map[y][x] = '.'
            map[y + dy][x + dx] = '@'
            map[y + k*dy][x + k*dx] = 'O'
            cur[0] = x + dx
            cur[1] = y + dy
        
def part1():
    map = []
    oper = ''
    first_part = True
    for line in open('input.txt'):
        if line == '\n':
            first_part = False
            continue
            
        if first_part:
            map.append(list(line.strip()))
        else:
            oper += line.strip()
            
    x = y = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                x, y = j, i
                break
            
    cur = [x, y]
    for dir in oper:
        move(map, dir, cur)

    ans = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'O':
                ans += 100 * i + j
                
    print(ans)


def moveable(map, cur, dx, dy):
    x, y = cur
    if map[y][x] == '#':
        return False
    
    if map[y][x] == '.':
        return True
    
    if dx != 0 or map[y][x] == '@':
        return moveable(map, [x + dx, y + dy], dx, dy)
    
    if map[y][x] == '[' and moveable(map, [x + dx, y + dy], dx, dy) and moveable(map, [x + dx + 1, y + dy], dx, dy):
        return True
        
    if map[y][x] == ']' and moveable(map, [x + dx, y + dy], dx, dy) and moveable(map, [x + dx - 1, y + dy], dx, dy):
        return True
        
    return False

def moveTo(map, cur, dx, dy):
    x, y = cur
    if map[y][x] == '#':
        return False
    
    if map[y][x] == '.':
        return True
    
    if dx != 0 or map[y][x] == '@':
        if moveTo(map, [x + dx, y + dy], dx, dy):
            map[y + dy][x + dx] = map[y][x]
            map[y][x] = '.'
            cur[0] = x + dx
            cur[1] = y + dy
            return True
        
        return False
    
    if map[y][x] == '[' and moveTo(map, [x + dx, y + dy], dx, dy) and moveTo(map, [x + dx + 1, y + dy], dx, dy):
        map[y + dy][x + dx:x + dx + 2] = ['[', ']']
        map[y][x:x + 2] = ['.', '.']
        return True
        
    if map[y][x] == ']' and moveTo(map, [x + dx, y + dy], dx, dy) and moveTo(map, [x + dx - 1, y + dy], dx, dy):
        map[y + dy][x + dx - 1:x + dx + 1] = ['[', ']']
        map[y][x - 1:x + 1] = ['.', '.']
        return True
        
    return False

def part2():
    map = []
    oper = ''
    first_part = True
    for line in open('input.txt'):
        if line == '\n':
            first_part = False
            continue
            
        if first_part:
            map.append(list(line.strip()))
        else:
            oper += line.strip()
            
    map2 = [[] for _ in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '#':
                map2[i] += ['#', '#']
            elif map[i][j] == 'O':
                map2[i] += ['[', ']']
            elif map[i][j] == '.':
                map2[i] += ['.', '.']
            else:
                map2[i] += ['@', '.']
            
    map = map2
    
    x = y = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '@':
                x, y = j, i
                break
                
    cur = [x, y]
    for dir in oper:
        dx, dy = diff(dir)
        if moveable(map, cur, dx, dy):
            moveTo(map, cur, dx, dy)

    ans = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '[':
                ans += 100 * i + j
                
    print(ans)

part2()