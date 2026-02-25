## 백준 2292 벌집 문제
target = int(input())
change_ = 1
counter = 1

while target > change_:
    change_ = change_ + 6*counter
    counter+=1

print(counter)

## 백준 9063 대지(여러 좌표 중에서 사각형 최소 넓이)
import sys

posX, posY = [] , []
time_ = int(input())
for i in range(time_):
    x,y = map(int, sys.stdin.readline().split())
    posX.append(x); posY.append(y)

xLength= max(posX)-min(posX); yLength = y=max(posY)-min(posY)
print(xLength * yLength)

## 백준 14215 세 막대기 
import sys

stick = list(map(int, sys.stdin.readline().split()))
max_ = max(stick); stick.remove(max_)
left_sum = stick[0] + stick[1]
if max_ < left_sum:
    stick.append(max_)
    print(sum(stick))
else:
    print(str(2*left_sum-1))
