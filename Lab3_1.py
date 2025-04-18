class Student:
    def __init__(self, name:str, student_id: int, grades:list):
        self.__name = name
        self.__student_id = student_id
        self.__grades = grades
    def add_grade(self, grade: int):
        if 0 <= grade <= 10:
            self.__grades.append(grade)
    def get_average(self):
        if self.__grades != []:
            return f'Средний балл:{sum(self.__grades)/len(self.__grades)}'
    def display_info(self):
        return f'Имя: {self.__name};\nНомер студента: {self.__student_id};\nОценка: {self.__grades}'

Nastya = Student(name='Настя', student_id=5, grades=[7,10,4])
print(Nastya.get_average())
print(Nastya.display_info())