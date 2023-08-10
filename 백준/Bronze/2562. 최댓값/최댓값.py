list = []

while True:
    a = int(input())
    list.append(a)
    if len(list) == 9 :
        break
    
MAX = max(list)
print(MAX)
print(list.index(MAX)+1)