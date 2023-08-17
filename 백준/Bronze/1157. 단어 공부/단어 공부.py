word = input().upper()
word_list = list(set(word))


cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])







# dict = {}
# for i in range(97,123):  # 알파벳에 0전부 넣기 소문자
#     dict[chr(i)] = 0
# # for i in range(65,91):  # 알파벳에 0전부 넣기 대문자
# #     dict[chr(i)] = 0
# # print(dict)


# word = input()
# low = word.lower()
# print(low)
# check = False 
# for i in range(len(word)):
#     if dict[low[i]] == 0 or dict[low[i]] > 0:
#         dict[low[i]] = dict[low[i]] + 1
        

# for i in dict:
#     # dict[i]와 dict의 맥스 value값이 같고, 그 둘 의 키값이 같지 않으면
#     if dict[i] == max(dict.values()) and dict.keys(max(dict.values())) != dict.keys(dict[i]) :
#         print("?")
#     else:
#         max_alpha = max(dict, key=dict.get)
#         print(max_alpha.upper())

