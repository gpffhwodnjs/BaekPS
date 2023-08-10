N,M = map(int, input().split())

cabinet = [i for i in range(1,N+1)]

# print(cabinet)

for _ in range(M):
    i,j = map(int, input().split())
    num = cabinet[i-1]
    cabinet[i-1] = cabinet[j-1]
    cabinet[j-1] = num

for i in range(0,N):
    print(cabinet[i],end=" ")
