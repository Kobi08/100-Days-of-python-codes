student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

count_sum = 0
total_num = 0

for n in student_heights:
  count_sum += n
print(count_sum)

for number_student in student_heights:
  total_num += 1
print(total_num)

avg = round(count_sum/total_num, 2)
print(avg)
  