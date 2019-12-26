n = int(input())
student_marks = {}
for i in range(n):
	name, *line = input().split()
	scores = list(map(float, line))
	student_marks[name] = scores
query_name = input()
if query_name in student_marks :
	r =0
	for i in range(3):
		r = r+scores[i]
	result = r/3
	print("{0:.2f}".format(result))

