n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
print(student_marks[query_name])
arr = student_marks[query_name]
s = sum(arr)
d = s/len(arr)
print(format(d, '.2f'))
