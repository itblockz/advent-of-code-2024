import re

def combo(operand, a, b, c):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c

def exec(a, b, c, program):
    pointer = 0
    out = []
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]
        
        match opcode:
            case 0: # adv
                a = a // 2**combo(operand, a, b, c)
            case 1: # bxl
                b = b ^ operand
            case 2: # bst
                b = combo(operand, a, b, c) % 8
            case 3: # jnz
                if a != 0:
                    pointer = operand
                    continue
            case 4: # bxc
                b = b ^ c
            case 5: # out
                out.append(combo(operand, a, b, c) % 8)
            case 6: # bdv
                b = a // 2**combo(operand, a, b, c)
            case 7: # cdv
                c = a // 2**combo(operand, a, b, c)
        
        pointer += 2

    return out

def part1():
    f = open('input.txt')
    a = int(re.search(r'\d+', f.readline()).group())
    b = int(re.search(r'\d+', f.readline()).group())
    c = int(re.search(r'\d+', f.readline()).group())
    f.readline()
    program = list(map(int, re.findall(r'\d', f.readline())))
    
    result = exec(a, b, c, program)
                        
    print(','.join(map(str, result)))
    
def dfs(min_a, val, b, c, program):
    for j in range(8):
        a = val + j
        result = exec(a, b, c, program)
        if result == program:
            min_a = min(min_a, a)
            return min_a
        if result[0] == program[-len(result)]:
            min_a = dfs(min_a, a * 8, b, c, program)
            
    return min_a
    
def part2():
    f = open('input.txt')
    f.readline()
    b = int(re.search(r'\d+', f.readline()).group())
    c = int(re.search(r'\d+', f.readline()).group())
    f.readline()
    program = list(map(int, re.findall(r'\d', f.readline())))
        
    min_a = float('inf')
    ans = dfs(min_a, 0, b, c, program)
    print(ans)
    
part2()