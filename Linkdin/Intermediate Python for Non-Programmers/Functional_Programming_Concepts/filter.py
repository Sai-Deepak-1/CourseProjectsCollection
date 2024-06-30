class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self): #https://docs.python.org/3/library/functions.html#repr
        return f"{self.name}: {self.score}"

students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Jane", 0.84), Student("Sarah", 0.63)]

fail_stu = []

for student in students:
    if student.score <= 0.7:
        fail_stu.append(student)

print(f"Failing Students via For Loop = {fail_stu}")

filter_fail_stu = list(filter(lambda x: x.score <= 0.7 ,students))
print(f"Failing Students via Filter   = {fail_stu}")

# Challenge
# Use filter to list all even numbers

numbers = [1,2,3,4,5]
print(f"EVen Numers are = {list(filter(lambda x: x%2==0, numbers))}")