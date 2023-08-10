# N = 바구니 갯수
# M = 공 넣을 횟수
# i 번 바구니부터 j번 바구니까지
# k번 번호의 공을 넣을 거임

N,M = map(int, input().split())

cabinet = [0 for _ in range(N)]


for _ in range(M):
    i,j,k = map(int, input().split())
    for n in range(i,j+1):
        cabinet[n-1] = k



for i in range(N):
    print(cabinet[i],end=" ")

