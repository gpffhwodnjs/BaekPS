# 킹 1개
# 퀸 1개
# 룩 2개
# 비숍 2개
# 나이트 2개
# 폰 8개
# 총 16개
# ex)0 1 2 2 2 7
# -> 1 0 0 0 0 1

ch = [ 1, 1, 2, 2, 2, 8]

D = list(map(int, input().split()))
piece = []
for i in range(0, len(D)):
    piece.append(ch[i] - D[i])
    print(piece[i],end=" ")
