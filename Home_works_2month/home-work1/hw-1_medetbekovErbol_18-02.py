# 1. Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
# 6. Добавить в класс Teacher атрибут уровня класса salary
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
# 10. Вызвать функцию create_student

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Full name: {self.fullname}, Age: {self.age}, Is married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks: dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def avearge(self):
        print(sum(self.marks.values()) // 5)

class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def get_finally_salary(self):
        if self.experience > 3:
            print(f'Salary + bonus: {self.salary // 100 * (5 * (self.experience - 3)) + self.salary}')
        else:
            print(f'Salary: {self.salary}')


student = Student('erbol medetbekov', 18, 'not', {'biology': 5})
print(f'Full name: {student.fullname}, Age: {student.age}, Is married: {student.is_married}, Marks: {student.marks}')
student.avearge()

teacher = Teacher('Erbol Medetbekov', 18, 'not married', 10)
print(f'Full name: {teacher.fullname}, Age: {teacher.age}, Is married: {teacher.is_married}, Salary: {teacher.salary}')
teacher.get_finally_salary()



def create_students():
    stud1 = Student(fullname='Kiril', age=18, is_married='not married', marks={
        'biology': 5,
        'chemistry': 5,
        'physics': 5,
        'mathematics': 5,
        'story': 5
    })
    stud2 = Student(fullname='John', age=16, is_married='not married', marks={
        'biology': 5,
        'chemistry': 4,
        'physics': 3,
        'mathematics': 3,
        'story': 2
    })
    stud3 = Student(fullname='Jack', age=19, is_married='not married', marks={
        'biology': 2,
        'chemistry': 3,
        'physics': 4,
        'mathematics': 5,
        'story': 2
    })

    result = [stud1, stud2, stud3]
    return result

for i in create_students():
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f'Name: {i.fullname}, Age: {i.age}, Married: {i.is_married}, Average marks: {sum(list)/len(list)}')
