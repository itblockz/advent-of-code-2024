def part1():
    disk_map = open("input.txt").read()
    disk = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk += [i // 2] * int(disk_map[i])
        else:
            disk += ['.'] * int(disk_map[i])
         
    l = 0
    r = len(disk) - 1
    
    while disk[l] != '.':
        l += 1
        
    while disk[r] == '.':
        r -= 1
    
    while l < r:
        disk[l], disk[r] = disk[r], disk[l]
        while disk[l] != '.':
            l += 1
            
        while disk[r] == '.':
            r -= 1
            
    ans = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            ans += i * int(disk[i])
        
    print(ans)

def part2():
    disk_map = open("input.txt").read()
    disk = []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            disk += [str(i // 2)] * int(disk_map[i])
        else:
            disk += ['.'] * int(disk_map[i])
         
    for i in reversed(range(len(disk_map) // 2 + 1)):
        print(i, len(disk_map) // 2 + 1)
        begin = disk.index(str(i))
        length = int(disk_map[i * 2])
        for j in range(len(disk) - length):
            if disk[j:j + length] == ['.'] * length and j < begin:
                disk[j:j + length] = [str(i)] * length
                disk[begin:begin + length] = ['.'] * length
                # print(''.join(disk))
                break
            
    ans = 0
    for i in range(len(disk)):
        print(i, len(disk))
        if disk[i] != '.':
            ans += i * int(disk[i])
        
    print(ans)

part2()