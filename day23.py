from collections import defaultdict

def part1():
    node = set()
    edge = set()
    for line in open('input.txt'):
        a, b = line.strip().split('-')
        node.add(a)
        node.add(b)
        edge.add((a, b))
        edge.add((b, a))
        
    ans = 0
        
    for a in node:
        for b in node:
            for c in node:
                if not a.startswith('t') and not b.startswith('t') and not c.startswith('t'):
                    continue
                if (a, b) in edge and (a, c) in edge and (b, c) in edge and (a, b, c):
                    ans += 1
                    
    print(ans // 6)
    
def dfs(group, node, edge, res):
    if len(res) == 13:
        return res
    
    if len(group) > len(res):
        res = list(group)
        
    for a in node:
        all_connect = True
        for b in group:
            if (a, b) not in edge:
                all_connect = False
                break
        if all_connect:
            group.append(a)
            res = dfs(group, node, edge, res)
            group.pop()
            
    return res

def bron_kerbosch(R, P, X, N, res):
    if not P and not X:
        if len(R) > len(res):
            res = list(R)
        return res
    
    for v in list(P):
        new_R = R | {v}
        new_P = P & N[v]
        new_X = X & N[v]
        res = bron_kerbosch(new_R, new_P, new_X, N, res)
        P = P - {v}
        X = X | {v}
        
    return res

def part2():
    node = set()
    graph = defaultdict(set)
    for line in open('input.txt'):
        a, b = line.strip().split('-')
        node.add(a)
        node.add(b)
        graph[a].add(b)
        graph[b].add(a)
    
    res = bron_kerbosch(set(), node, set(), graph, [])
    res.sort()
    ans = ','.join(res)
    print(ans)
    
part2()