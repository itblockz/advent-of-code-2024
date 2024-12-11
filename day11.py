from collections import defaultdict

def part1():
    A = list(map(int, open("input.txt").readline().split()))
    n = 25
    for i in range(n):
        B = []
        for a in A:
            if a == 0:
                B.append(1)
            elif len(str(a)) % 2 == 0:
                s = str(a)
                m = len(s)
                B.append(int(s[:m//2]))
                B.append(int(s[m//2:]))
            else:
                B.append(a * 2024)
                
        A = B
    
    print(len(A))
    
def part2():
    A = list(map(int, open("input.txt").readline().split()))
    cnt = defaultdict(int)
    
    for a in A:
        cnt[a] += 1
    
    for _ in range(75):
        cnt2 = defaultdict(int)
        for k, v in cnt.items():
            if k == 0:
                cnt2[1] += v
            elif len(str(k)) % 2 == 0:
                s = str(k)
                n = len(s)
                cnt2[int(s[:n//2])] += v
                cnt2[int(s[n//2:])] += v
            else:
                cnt2[k * 2024] += v
                
            cnt = cnt2
                
    print(sum(cnt.values()))
    
part2()