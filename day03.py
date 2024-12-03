import re

def util(str):
    return map(int, re.findall(r"\d+",str))

def part1():
    f = open("input.txt")
    ans = 0
    for x in f:
        A = map(util, re.findall(r"mul\(\d{1,3},\d{1,3}\)", x))
        for a, b in A:
            ans += a * b
            
    print(ans)
    
def part2():
    f = open("input.txt")
    ans = 0
    enable = True
    for x in f:
        A = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", x)
        for x in A:
            if x == "do()":
                enable = True
            elif x == "don't()":
                enable = False
            elif enable:
                a, b = map(int, re.findall(r"\d+", x))
                ans += a * b
                    
    print(ans)

part2()