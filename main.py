class Student:
    l_student = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.l_student.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.coursses_grades:
                lecturer.coursses_grades[course] += [grade]
            else:
                lecturer.coursses_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        counter = 0
        summa = 0
        for a in self.grades:
            for b in self.grades.get(a):
                counter += 1
                summa += b
        return summa / counter

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за ДЗ: {self.average_grades()}')
        print(f'Курсы в процессе изучения: {self.courses_in_progress}')
        print(f'Завершенные курсы: {self.finished_courses}')
        return ''


class Mentor:
    def __init__(self):
        name = ''
        surname = ''
        courses_attached = ''


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.coursses_grades = {}


    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за лекции: {str(self.average_grades())}')
        return ''

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.average_grades() < other.average_grades()

    def average_grades(self):
        counter = 0
        summa = 0
        for a in self.coursses_grades:
            for b in self.coursses_grades.get(a):
                counter += 1
                summa += b
        return summa / counter


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        return ''

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Pam', 'Param')
best_student2 = Student('Pam2', 'Param2')
best_reviewer = Reviewer('Param', 'Pam')
best_reviewer2 = Reviewer('Param2', 'Pam2')
best_lecturer = Lecturer('Pam', 'Pam')
best_lecturer2 = Lecturer('Pam2', 'Pam2')


best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Java']

best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Java']
best_reviewer2.courses_attached += ['Python']
best_reviewer2.courses_attached += ['Java']

best_lecturer.courses_attached += ['Java']
best_lecturer.courses_attached += ['Python']
best_lecturer2.courses_attached += ['Java']
best_lecturer2.courses_attached += ['Python']


best_reviewer.rate_hw(best_student, 'Java', 10)
best_reviewer.rate_hw(best_student, 'Java', 5)
best_reviewer.rate_hw(best_student, 'Java', 2)
best_reviewer.rate_hw(best_student, 'Java', 3)

best_student.rate_lecturer(best_lecturer2, 'Java', 10)
best_student.rate_lecturer(best_lecturer2, 'Java', 3)
best_student.rate_lecturer(best_lecturer2, 'Java', 6)
best_student.rate_lecturer(best_lecturer2, 'Java', 2)

best_student.rate_lecturer(best_lecturer2, 'Python', 2)
best_student.rate_lecturer(best_lecturer2, 'Python', 4)
best_student.rate_lecturer(best_lecturer2, 'Python', 4)
best_student.rate_lecturer(best_lecturer2, 'Python', 4)



best_student.rate_lecturer(best_lecturer, 'Java', 10)
best_student.rate_lecturer(best_lecturer, 'Java', 5)
best_student.rate_lecturer(best_lecturer, 'Java', 7)
best_student.rate_lecturer(best_lecturer, 'Java', 3)

best_student.rate_lecturer(best_lecturer, 'Python', 9)
best_student.rate_lecturer(best_lecturer, 'Python', 9)
best_student.rate_lecturer(best_lecturer, 'Python', 9)
best_student.rate_lecturer(best_lecturer, 'Python', 9)








#print(best_lecturer < best_lecturer2)



#print(best_student)
#print(best_reviewer)
#print(best_lecturer)



