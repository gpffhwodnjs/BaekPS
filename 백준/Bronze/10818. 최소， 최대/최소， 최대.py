N = int(input())
list = list(map(int, input().split()))

list_slice = list[0:N]

print(min(list_slice),max(list_slice))
