# n , m = map(int, input().split())

# arr_1 = []
# arr_2 = []
# result = []
# for i in range(n):
#     arr_1.append(list(map(int, input().split())))

# for i in range(n):
#     arr_2.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(m):
#         result.append(arr_1[i][j] + arr_2[i][j])
# print(result)
    

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]
# print(a)
# print(b)
for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for i in a:
    print(*i)