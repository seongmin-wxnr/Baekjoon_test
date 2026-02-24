import sys

arr = [[0]*100 for _ in range(100)]
time_ = int(input())

for i in range(time_):
    posX,posY = map(int, sys.stdin.readline().split())
    for i in range(posX , posX+10):
        for j in range(posY , posY+10):
            arr[i][j] = 1

total = 0
for i in range(100):
    total = total + arr[i].count(1)
print(total)
