class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


students = [
    Student("Joe", 0.46),
    Student("Amy", 0.72),
    Student("Mark", 0.88),
    Student("Zach", 0.75),
    Student("Jane", 0.84),
    Student("Sarah", 0.63),
]

results = []
for student in students:
    results.append(f"{student.name} Passed" if student.score>=0.7 else f"{student.name} Failed")


map_res = list(map(lambda student: f"{student.name} Passed" if student.score>=0.7 else f"{student.name} Failed", students))

print(f"For Loop Results are = {results}")
print(f"Map Results are      = {map_res}")

# Challenge
# Use map to mulltiply all these numbers by 2

numbers = [1, 2, 3, 4, 5]

res = list(map(lambda x: x*2, numbers))
print(res)