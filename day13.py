import re

def part1():
    ans = 0
    file = open('input.txt')
    while True:
        a, d = map(int, re.findall(r'\d+', file.readline()))
        b, e = map(int, re.findall(r'\d+', file.readline()))
        c, f = map(int, re.findall(r'\d+', file.readline()))
        x = 0
        y = (c - b*x) / a
        while y >= 0:
            if y == int(y) and a*y + b*x == c and d*y + e*x == f:
                ans += 3 * int(y) + x
                break
                
            x += 1
            y = (c - b*x) / a
                
        if file.readline() != '\n':
            break
        
    print(ans)
    
def part2():
    ans = 0
    file = open('input.txt')
    while True:
        a, d = map(int, re.findall(r'\d+', file.readline()))
        b, e = map(int, re.findall(r'\d+', file.readline()))
        c, f = map(int, re.findall(r'\d+', file.readline()))
        c += 10000000000000
        f += 10000000000000
        
        # solve ax + by = c and dx + ey = f
        x = (b*f - c*e) / (b*d - a*e)
        y = (c - a*x) / b
        
        if x == int(x) and y == int(y):
            ans += 3 * int(x) + int(y)
            
        if file.readline() != '\n':
            break
        
    print(ans)
    
part2()