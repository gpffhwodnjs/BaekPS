students = []

for i in range(1,31) :
    students.append(i)

while True :
    n = int(input())
    students.remove(n)
    if len(students) == 2 :
        break

print(min(students))
print(max(students))

