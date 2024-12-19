def possible(desired:str, towels):
    towel_set = {''}
    while towel_set:
        cur = towel_set.pop()
        if len(cur) > len(desired):
            continue
        if desired == cur:
            return True
        if desired.startswith(cur):
            for tw in towels:
                towel_set.add(cur + tw)
                
    return False

def part1():
    f = open('input.txt')
    towels = f.readline().strip().split(', ')
    f.readline()
    ans = 0
    for line in f:
        desired = line.strip()
        if possible(desired, towels):
            ans += 1
            
    print(ans)
    
def possible_num(desired:str, towels):
    cnt = {'' : 1}
    for i in range(1, len(desired) + 1):
        sub = desired[:i]
        cnt[sub] = 0
        for tw in towels:
            if sub.endswith(tw):
                cnt[sub] += cnt[sub[:sub.rfind(tw)]]

    return cnt[desired]
    
def part2():
    f = open('input.txt')
    towels = f.readline().strip().split(', ')
    f.readline()
    ans = 0
    for line in f:
        desired = line.strip()
        ans += possible_num(desired, towels)
            
    print(ans)
    
part2()