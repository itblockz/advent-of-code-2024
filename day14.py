import re
import numpy as np
import cv2

def part1():
    w, h = 101, 103
    Q = [[0, 0], [0, 0]]
    for line in open('input.txt'):
        px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
        t = 100
        x = (vx * t + px) % w
        y = (vy * t + py) % h
        if x != w // 2 and y != h // 2:
            Q[y // ((h + 1) // 2)][x // ((w + 1) // 2)] += 1
    
    ans = Q[0][0] * Q[0][1] * Q[1][0] * Q[1][1]
    
    print(ans)
        
def part2():
    w, h = 101, 103
    for t in range(10000):
        A = [[0] * w for _ in range(h)]
        Q = [[0, 0], [0, 0]]
        for line in open('input.txt'):
            px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
            x = (vx * t + px) % w
            y = (vy * t + py) % h
            if x != w // 2 and y != h // 2:
                Q[y // ((h + 1) // 2)][x // ((w + 1) // 2)] += 1
            A[y][x] += 1
            
        matrix = np.array(A, dtype=np.float32)
        matrix_normalized = (matrix - matrix.min()) / (matrix.max() - matrix.min()) * 255
        gray_image = matrix_normalized.astype(np.uint8)
        
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        
        _, binary_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)
        
        if np.any(binary_image != 0):
            print(t)
        
part2()