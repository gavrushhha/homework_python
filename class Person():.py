class Person():
    def __init__(self, name):
        self.name = name
class Student(Person):
    know = 0
    homework = 0
    def get_know(self):
        self.know+=1
    def get_homework(self, n):
        self.homework+=n
    def do_homework(self):
        if self.homework > 0:
            self.homework-=1
            self.get_know()
        else:
            print('No homework!')
class Teacher(Person):
    work = 0
    def give_know(self, students):
        for student in students:
            student.get_know()
            self.work+=1
    def give_homework(self, students, n):
        for student in students:
            student.get_homework(n)
            self.work+=1
t = Teacher('Petr')
st_1 = Student('Ivan')
st_2 = Student('Maria')
t.give_know([st_1, st_2])
print(t.work)
print(st_1.know)