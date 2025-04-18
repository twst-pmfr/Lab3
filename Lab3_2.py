class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

class Teacher(Person):
    def __init__(self, subject: str, students: str, name: str, age: int):
        super().__init__(name, age)
        self.__subject = subject
        self.__students = students
    def add_student(self, student: str):
        if student not in self.__students:
            return self.__students.append(student)

    def remove_student(self, student: str):
        if student in self.__students:
            return self.__students.remove(student)


    def list_students(self, student):
        for student in self.students:
            print(student.introduce())


