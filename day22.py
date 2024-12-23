from collections import defaultdict

def mix(num, res):
    return num ^ res

def prune(num):
    return num % 16777216

def secret(num):
    res = num * 64
    num = mix(num, res)
    num = prune(num)
    
    res = num // 32
    num = mix(num, res)
    num = prune(num)
    
    res = num * 2048
    num = mix(num, res)
    num = prune(num)
    
    return num

def part1():
    ans = 0
    for line in open('input.txt'):
        num = int(line.strip())
        for _ in range(2000):
            num = secret(num)
        ans += num
    print(ans)
     
def part2():
    cnt = defaultdict(int)
    for line in open('input.txt'):
        buf = []
        num = int(line.strip())
        prev = num % 10
        visited = set()
        for _ in range(2000):
            num = secret(num)
            diff = (num % 10) - prev
            prev = num % 10
            if len(buf) == 4:
                buf.pop(0)
            buf.append(diff)
            key = tuple(buf)
            if len(key) == 4 and key not in visited:
                cnt[key] += prev
                visited.add(key)
    ans = max(cnt.values())
    print(ans)

part2()