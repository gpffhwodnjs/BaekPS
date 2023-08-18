# 알파벳이 한개만 나오거나 연속해서 나오면 그룹단어
# 한번 나온 알파벳은 다른 알파벳 뒤에나오면 안됨    
N = int(input())
cnt = N  # 그룹단어에 해당하는 걸 세는게 아니라
        # 그룹단어가 아닌 걸 빼버릴거임

for i in range(N):
    word = input()
    for j in range(len(word)-1): # 마지막 글자는 비교할 필요가 없음
        if word[j] == word[j+1]:
            pass # 그냥 넘어가면 됨
        elif word[j] in word[j+1:]: # 현재 단어 뒤에 현재 단어가 있으면 그룹단어가 아니기 때문에 -1
            cnt -= 1
            break

print(cnt)


# 스쳐온 바보같은 과거들
# N = int(input())
# cnt = 0


# for i in range(N):
    
#     word = input()
#     for j in range(len(word)-1):
#         check = []
#         if word[j] not in check:
#             if (word[j] == word[j+1]) and (word[j+1] not in check) :
#                 cnt += 1
#                 print(cnt)
#                 check.append(word[j])
#             elif (word[j] != word[j+1]) and (word[j+1] not in check):
#                 cnt += 1
#                 print(cnt)
#                 check.append(word[j])
#         else:
#             print("다른경우")
         
    
# aca
# a  -- 들어있지않음
# a =/ c 이기때문에 cnt += 1
# [a, ,]


# c -- 들어있지않음
# c =/ a 이기때문에 cnt += 1 이 되면 안됨 왜? a가 이미 있기때문에
# 그러면 a가 없을때 넣어줘야함 not in check
       
# a -- 들어있음= 아무것도 안 함 끝.
         
    

    
