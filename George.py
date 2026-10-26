name = "Kardelen"
age = 36.5
height = 1.65
student_now = True
city = "Poznan"
print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type(student_now))
print(type(city))

slices_per_student = 3
students = 20
enrolled_students = students + 3
present_students = enrolled_students - 2
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order * 8) % present_students
print("Enrolled students:", enrolled_students)
print("Present students:", present_students)
print("Total slices needed:", total_slices_needed)
print("Cost per student:", cost_per_student)
print("Boxes to order:", boxes_to_order)
print("Leftover slices:", leftover_slices) 
