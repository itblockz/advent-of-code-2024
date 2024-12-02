f = open("input.txt")

def part1():
    ans = 0
    for report in f:
        safe = True
        levels = list(map(int, report.split()))
        if (levels[0] == levels[1]):
            continue
        
        inc = levels[0] < levels[1]
        for i in range(1, len(levels)):
            if inc and levels[i - 1] >= levels[i]:
                safe = False
                break
            elif not inc and levels[i - 1] <= levels[i]:
                safe = False
                break
            elif abs(levels[i] - levels[i - 1]) < 1 or abs(levels[i] - levels[i - 1]) > 3:
                safe = False
                break
                
        if safe:
            ans += 1

    print(ans)

def is_safe(levels):
    if (levels[0] == levels[1]):
        return False
    
    inc = levels[0] < levels[1]
    for i in range(1, len(levels)):
        if inc and levels[i - 1] >= levels[i]:
            return False
        elif not inc and levels[i - 1] <= levels[i]:
            return False
        elif abs(levels[i] - levels[i - 1]) < 1 or abs(levels[i] - levels[i - 1]) > 3:
            return False
            
    return True

def part2():
    ans = 0
    for report in f:
        safe = True
        levels = list(map(int, report.split()))
        for i in range(len(levels)):
            copy = list(levels)
            copy.pop(i)
            if is_safe(copy):
                ans += 1
                break

    print(ans)

part2()