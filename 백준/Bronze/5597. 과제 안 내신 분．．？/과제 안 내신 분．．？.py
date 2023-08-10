students = []

for i in range(1,31) :
    students.append(i)

#더 간단한 방법
# 1. students = list(range(1,31))
# 2. students = [i for i in range(1,31)]

while True :
    n = int(input())
    students.remove(n)
    if len(students) == 2 :
        break

print(min(students))
print(max(students))

