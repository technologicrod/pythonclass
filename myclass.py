class Student:
    student_count = 0 
    def __init__(self, newName, newGrades):
        self.fullName = newName
        self.grades = newGrades
        Student.student_count += 1
    def getAverage(self):
        return sum(self.grades) / len(self.grades)
    def getName(self):
        return self.fullName

st_one = Student("Ogs Ablazo", [77,74,80,98])
st_two = Student("Skusta Clee", [90, 92, 95, 100])
print(st_one.getAverage())
print(st_one.getName())
print(Student.student_count)

print(st_two.getAverage())
print(st_two.getName())
print(Student.student_count)

