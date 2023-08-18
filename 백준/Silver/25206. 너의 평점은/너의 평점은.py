
# 평점 : (과목 이수학점 x 과목 성적점수) /  학점의 총합
#         (credit x result) / total_score

# rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
# grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

dict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}

total_score = 0	
result = 0
for _ in range(20) :
    dpet, credit, grade = input().split()
    credit = float(credit)
    if grade != 'P' :
        total_score += credit
        result += credit * dict[grade]

print('%.6f' % (result / total_score))