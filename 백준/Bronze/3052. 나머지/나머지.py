list = []
while True:
    n = int(input())
    list.append(n)
    if len(list) == 10 :
        break

list_list = []
for i in range(10):
    list_list.append((list[i])%42)
    
fin = set(list_list)
print(len(fin))

