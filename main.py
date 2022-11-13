class Student:
    l_student = []
    l_avg_grades = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grades = 0
        self.l_student.append(self)
        self.l_avg_grades.append(self.avg_grades)

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
        self.avg_grades = summa / counter
        return self.avg_grades

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Средняя оценка за ДЗ: {self.avg_grades}')
        print(f'Курсы в процессе изучения: {self.courses_in_progress}')
        print(f'Завершенные курсы: {self.finished_courses}')
        return ''

    def course_avg(self, students_list, course_name):
        summa = 0
        counter = 0
        if course_name in self.courses_in_progress:
            for a in students_list:
                print(a.grades.get(course_name))
                for i in a.grades.get(course_name):
                    summa += i
                    counter += 1
        else:
            return 'Ошибка'
        return summa / counter


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

    def course_avg(self, lecturer_list, course_name):
        summa = 0
        counter = 0
        if course_name in self.courses_attached:
            for a in lecturer_list:
                print(a.coursses_grades.get(course_name))
                for i in a.coursses_grades.get(course_name):
                    summa += i
                    counter += 1
        else:
            return 'Ошибка'
        return summa / counter
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
best_student_2 = Student('Pam2', 'Param2')
best_reviewer = Reviewer('Param', 'Pam')
best_reviewer_2 = Reviewer('Param2', 'Pam2')
best_lecturer = Lecturer('Pam', 'Pam')
best_lecturer_2 = Lecturer('Pam2', 'Pam2')


best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Java']

best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Java']
best_reviewer_2.courses_attached += ['Python']
best_reviewer_2.courses_attached += ['Java']

best_lecturer.courses_attached += ['Java']
best_lecturer.courses_attached += ['Python']
best_lecturer_2.courses_attached += ['Java']
best_lecturer_2.courses_attached += ['Python']


best_reviewer.rate_hw(best_student, 'Java', 10)
best_reviewer.rate_hw(best_student, 'Java', 5)
best_reviewer.rate_hw(best_student, 'Java', 2)
best_reviewer.rate_hw(best_student, 'Java', 3)
best_reviewer_2.rate_hw(best_student_2, 'Java', 10)
best_reviewer_2.rate_hw(best_student_2, 'Java', 10)
best_reviewer_2.rate_hw(best_student_2, 'Java', 2)
best_reviewer_2.rate_hw(best_student_2, 'Java', 5)

best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 5)
best_reviewer.rate_hw(best_student, 'Python', 5)
best_reviewer_2.rate_hw(best_student_2, 'Python', 10)
best_reviewer_2.rate_hw(best_student_2, 'Python', 10)
best_reviewer_2.rate_hw(best_student_2, 'Python', 3)
best_reviewer_2.rate_hw(best_student_2, 'Python', 3)

best_student.rate_lecturer(best_lecturer, 'Java', 10)
best_student.rate_lecturer(best_lecturer, 'Java', 3)
best_student.rate_lecturer(best_lecturer, 'Java', 6)
best_student.rate_lecturer(best_lecturer, 'Java', 2)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 5)
best_student.rate_lecturer(best_lecturer, 'Python', 6)
best_student.rate_lecturer(best_lecturer, 'Python', 8)

best_student_2.rate_lecturer(best_lecturer_2, 'Java', 10)
best_student_2.rate_lecturer(best_lecturer_2, 'Java', 10)
best_student_2.rate_lecturer(best_lecturer_2, 'Java', 4)
best_student_2.rate_lecturer(best_lecturer_2, 'Java', 4)
best_student_2.rate_lecturer(best_lecturer_2, 'Python', 2)
best_student_2.rate_lecturer(best_lecturer_2, 'Python', 4)
best_student_2.rate_lecturer(best_lecturer_2, 'Python', 4)
best_student_2.rate_lecturer(best_lecturer_2, 'Python', 4)


print(best_student.average_grades())
print(best_student_2.average_grades())

print(best_lecturer.average_grades())
print(best_lecturer_2.average_grades())

print(best_student.course_avg([best_student, best_student_2], 'Python'))
print(best_lecturer.course_avg([best_lecturer, best_lecturer_2], 'Java'))

print(best_student)
print(best_student_2)

print(best_lecturer)
print(best_lecturer_2)

print(best_reviewer)
print(best_reviewer_2)

print(best_lecturer < best_lecturer_2)
print(best_lecturer > best_lecturer_2)
