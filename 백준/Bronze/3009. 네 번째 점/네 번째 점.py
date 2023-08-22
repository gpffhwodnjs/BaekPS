x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

#축과 평행한 직사각형의 꼭지점을 찾는 문제
#x축과 y축을 따로 생각해보자
#x축의 경우 x1,x2,x3가 주어지고 y축의 경우 y1,y2,y3가 주어진다.
#
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
elif x2 == x3:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
elif y2 == y3:
    y4 = y1

print(x4,y4)        