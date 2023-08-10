test = int(input())

while True:
    score = list(map(float, input().split()))
    if len(score) == test :
        break
    else :
        continue

MAX = max(score)

Re_score = []
for i in range(len(score)):
    Re_score.append(score[i]/MAX*100)


print(sum(Re_score)/len(Re_score))