S = input()
#ABCD

#다시 생각해보기
# dial = ['ABC', 
#        'DEF', 
#        'GHI', 
#        'JKL', 
#        'MNO', 
#        'PQRS', 
#        'TUV', 
#        'WXYZ']


#########  멍청한 방법  ##########
sum_sum = 0
dial = 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
for i in range(0,len(S)):
    for k in range(0,len(dial)):
        if S[i] == dial[k] :
            #  print(dial.index(dial[k]))
            if 0<=dial.index(dial[k])<=2 :
                T = 3
            elif 3<=dial.index(dial[k])<=5 :
                T = 4
            elif 6<=dial.index(dial[k])<=8 :
                T = 5
            elif 9<=dial.index(dial[k])<=11 :
                T = 6
            elif 12<=dial.index(dial[k])<=14 :
                T = 7
            elif 15<=dial.index(dial[k])<=18 :
                T = 8
            elif 19<=dial.index(dial[k])<=21 :
                T = 9 
            else :
                T = 10
            sum_sum = sum_sum + T
print(sum_sum)