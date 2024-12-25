import re

wires = {}
initial_wires = {}
initial_wires_str = {}
relation = {}
wires_str = {}

def init():
    f = open('input.txt')
    line = f.readline().strip()
    while line != '':
        name, val = line.split(': ')
        line = f.readline().strip()
        wires[name] = int(val)
        initial_wires[name] = int(val)
        wires_str[name] = name
        initial_wires_str[name] = name
        
    line = f.readline().strip()
    while line != '':
        a, gate, b, c = re.split(r' -> | ', line)
        relation[c] = (gate, a, b)
        line = f.readline().strip()

def dfs(out):
    if out in wires:
        return wires[out]
    gate, a, b = relation[out]
    match gate:
        case 'OR':
            res = dfs(a) | dfs(b)
        case 'AND':
            res = dfs(a) & dfs(b)
        case 'XOR':
            res = dfs(a) ^ dfs(b)
    wires[out] = res
    return res

def part1():
    init()
    z_wire = list(filter(lambda w:w.startswith('z'), relation.keys()))
    z_wire.sort(reverse=True)
    z_wire = map(lambda z:str(dfs(z)), z_wire)
    ans = int(''.join(z_wire), 2)
    print(ans)
    
def swap(a, b):
    relation[a], relation[b] = relation[b], relation[a]
    global wires, wires_str
    wires = initial_wires.copy()
    wires_str = initial_wires_str.copy()
    
def compute():
    z_wire = list(filter(lambda w:w.startswith('z'), relation.keys()))
    z_wire.sort(reverse=True)
    z_wire = map(lambda z:str(dfs(z)), z_wire)
    z_num = int(''.join(z_wire), 2)
    return z_num

def dfs2(out):
    if out in wires_str:
        return wires_str[out]
    gate, a, b = relation[out]
    val = [dfs2(a), dfs2(b)]
    val.sort()
    match gate:
        case 'OR':
            res = f'({val[0]} | {val[1]})'
        case 'AND':
            res = f'({val[0]} & {val[1]})'
        case 'XOR':
            res = f'({val[0]} ^ {val[1]})'
    wires_str[out] = res
    return res
            
def part2():
    init()
    
    x_wire = list(filter(lambda w:w[0].startswith('x'), wires.items()))
    x_wire.reverse()
    x_wire = map(lambda w:str(w[1]), x_wire)
    x_num = int(''.join(x_wire), 2)
    
    y_wire = list(filter(lambda w:w[0].startswith('y'), wires.items()))
    y_wire.reverse()
    y_wire = map(lambda w:str(w[1]), y_wire)
    y_num = int(''.join(y_wire), 2)
    
    z_wire = list(filter(lambda w:w.startswith('z'), relation.keys()))
    z_wire.sort(reverse=True)
    
    swap('z18', 'kvn')
    swap('hbk', 'z14')
    swap('z23', 'dbb')
    swap('cvh', 'tfn')
    
    for z in z_wire:
        dfs2(z)
        # print(z, wires_str[z])
        
    # z_num = compute()
    # print(bin(z_num))
    # print(bin(x_num + y_num))
    # print(z_num - (x_num + y_num))
    
    # print(len('10000111100011011100110'))
    # print(len('0010011011110000111100011011100110'))
    
    res = ['z18', 'kvn', 'hbk', 'z14', 'z23', 'dbb', 'cvh', 'tfn']
    res.sort()
    ans = ','.join(res)
    print(ans)
    
part2()