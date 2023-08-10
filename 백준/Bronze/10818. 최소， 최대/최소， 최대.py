N = int(input())
list = list(map(int, input().split()))

list_slice = list[0:N]
#(추가) 굳이 slice 해주지 않았어도된다고 한다.

print(min(list_slice),max(list_slice))
