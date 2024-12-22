import re
from collections import deque

def diff(c):
    return {
        '^':(0, -1),
        'v':(0, 1),
        '<':(-1, 0),
        '>':(1, 0)
    }[c]

def num_pad(code, num_mem):
    num = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [' ', '0', 'A']
    ]
    
    if code == '':
        return ''
    
    res, x, y = num_mem[code[:-1]]
    
    if x < 0 or x >= 3 or y < 0 or y >= 4 or num[y][x] == ' ':
        return None
    
    c = code[-1]
    if c == 'A':
        res += num[y][x]
    else:
        dx, dy = diff(c)
        x += dx
        y += dy
        
    num_mem[code] = res, x, y
    return res
    
def dir_pad(code, dir_mem):
    dir = [
        [' ', '^', 'A'],
        ['<', 'v', '>']
    ]
    
    if code == '':
        return ''
    
    res, x, y = dir_mem[code[:-1]]
    
    c = code[-1]
    if x < 0 or x >= 3 or y < 0 or y >= 2 or dir[y][x] == ' ':
        return None
    
    if c == 'A':
        res += dir[y][x]
    else:
        dx, dy = diff(c)
        x += dx
        y += dy
        
    dir_mem[code] = res, x, y
    return res
    
def bfs(target: str, pad, collect=-1):
    queue = deque([''])
    num_mem = {'': ('', 2, 3)}
    dir_mem = {'': ('', 2, 0)}
    best_res = 0
    best_code = float('inf')
    res_list = []
    while queue:
        code = queue.popleft()
        
        if len(code) > best_code:
            continue
        
        res = code
        
        if pad == 0:
            if re.match(r'.*[<v>^]{6}', res):
                continue
            
            res = num_pad(res, num_mem)
        
            recent = re.search(r'(?<=A)[<v>\^]*$', code).group() if 'A' in code else code
        
            if ('<' in recent and '>' in recent) or ('^' in recent and 'v' in recent):
                continue
        else:
            if re.match(r'.*[<v>^]{4}', res):
                continue
            
            res = dir_pad(res, dir_mem)
        
            recent = re.search(r'(?<=A)[<v>\^]*$', code).group() if 'A' in code else code
        
            if ('<' in recent and '>' in recent) or ('^' in recent and 'v' in recent):
                continue
            
        if res == target:
            best_code = len(code)
            res_list.append(code)
            if len(res_list) == collect:
                return res_list
            continue
        
        if res is not None and target.startswith(res) and len(res) < len(target) and len(res) >= best_res:
            best_res = len(res)
            for move in 'A<v>^':
                queue.append(code + move)
                
    return res_list
    
def part1():
    ans = 0
    for line in open('input.txt'):
        target = line.strip()
        num = int(target[:3])
        
        candidates = bfs(target, 0)
        res = []
        for code in candidates:
            candidates2 = bfs(code, 1)
            if len(res) == 0 or len(candidates2[0]) < len(res[0]):
                res = candidates2
            elif len(candidates2[0]) == len(res[0]):
                res += candidates2
                
        candidates = res
        best = float('inf')
        for code in candidates:
            candidates2 = bfs(code, 1, 1)
            best = min(best, len(candidates2[0]))
        
        ans += best * num
        
    print(ans)
    
def num_pad_code():
    num = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [' ', '0', 'A']
    ]
    code = {}
    for y1 in range(4):
        for x1 in range(3):
            for y2 in range(4):
                for x2 in range(3):
                    vdir = ('^' if y2 - y1 < 0 else 'v') * abs(y2 - y1)
                    hdir = ('<' if x2 - x1 < 0 else '>') * abs(x2 - x1)
                    paths = set([vdir + hdir, hdir + vdir])
                    paths = list(map(lambda x:x + 'A', filter(lambda p:panic(p, x1, y1, 0, 3), paths)))
                    code[(num[y1][x1], num[y2][x2])] = paths
    return code

def dir_pad_code():
    dir = [
        [' ', '^', 'A'],
        ['<', 'v', '>'],
    ]
    code = {}
    for y1 in range(2):
        for x1 in range(3):
            for y2 in range(2):
                for x2 in range(3):
                    vdir = ('^' if y2 - y1 < 0 else 'v') * abs(y2 - y1)
                    hdir = ('<' if x2 - x1 < 0 else '>') * abs(x2 - x1)
                    paths = set([vdir + hdir, hdir + vdir])
                    paths = list(map(lambda x:x + 'A', filter(lambda p:panic(p, x1, y1, 0, 0), paths)))
                    code[(dir[y1][x1], dir[y2][x2])] = paths
    return code

def panic(path, x, y, px, py):
    for c in path:
        dx, dy = diff(c)
        x += dx
        y += dy
        if x == px and y == py:
            return False
    return True

mem = {}

def relay(codes, remain):
    if remain == 0:
        return min(map(len, codes))
    min_length = float('inf')
    for code in codes:
        length = 0
        code = 'A' + code
        for i in range(len(code) - 1):
            key = (code[i], code[i + 1], remain)
            if key in mem:
                step = mem[key]
            else:
                dir = dir_code[(code[i], code[i + 1])]
                step = relay(dir, remain - 1)
                mem[key] = step
            length += step
        min_length = min(min_length, length)
    return min_length

num_code = num_pad_code()
dir_code = dir_pad_code()

def part2():
    ans = 0
    for line in open('input.txt'):
        length = 0
        code = line.strip()
        code = 'A' + code
        for i in range(len(code) - 1):
            num = num_code[(code[i], code[i + 1])]
            step = relay(num, 25)
            length += step
        ans += length * int(code[1:4])
    print(ans)
    
part2()