N,M = map(int, input().split())

cabinet = [i for i in range(1,N+1)]

# 5 4
# 1 2 3 4 5

# 1 2     2 1 3 4 5
# 3 4     2 1 4 3 5
# 1 4     3 4 1 2 5
# 2 2     3 4 1 2 5

for _ in range(M):
    i,j = map(int, input().split())
    cabinet_slice = cabinet[i-1:j]
    cabinet_slice.reverse()
    cabinet[i-1:j] = cabinet_slice
    # print(cabinet)

#print(cabinet)

for i in range(0,N):
    print(cabinet[i],end=" ")
    