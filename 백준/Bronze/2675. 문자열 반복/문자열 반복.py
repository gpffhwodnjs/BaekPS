# T = 테스트 케이스
# S = 문자열
# R = 반복 횟수

T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    # print(R, list(S))
    for j in range(len(S)):
        P = S[j]
        print(P*R,end="")
    print("")