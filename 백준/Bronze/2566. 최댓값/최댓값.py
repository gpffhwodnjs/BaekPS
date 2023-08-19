a = [list(map(int,input().split())) for _ in range(9)]

max = 0

for i in range(9):
    for j in range(9):
        if a[i][j] >= max: 
            max = a[i][j] #모든 값 비교하면서 큰 값 저장
            c = i          #최댓값의 인덱스 저장
            r = j
print(max)  
print(c+1,r+1)  #인덱스는 0부터 시작하니까 +1 해줌

