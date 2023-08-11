T = int(input())

#abcdefg
#0123456
#7

for i in range(T) :
    S = input()
    a = S[0]
    b = len(S)-1
    #출력문에 공백 지워야됨
    print (a,S[b],sep="")