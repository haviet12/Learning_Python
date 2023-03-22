# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total_height=0
for n in range(0, len(student_heights)):

    total_height = total_height + int(student_heights[n])
    average_height= total_height / (n + 1)

print(f"chiều cao trung bình là: {round(average_height)}")

