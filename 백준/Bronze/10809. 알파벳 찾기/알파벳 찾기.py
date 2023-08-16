#딕셔너리

dict = {}
for i in range(97,123):  # 알파벳에 -1 전부 넣기
    dict[chr(i)] = -1

# print(dict)
S = input()
for i in range(len(S)):
    if dict[S[i]] == -1:
        dict[S[i]] =i
    
# print(*dict.values())    

for i in range(97,123):
    print(dict[chr(i)],end=' ')