import self as self


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades2:
                lecturer.grades2[course] += [grade]
            else:
                lecturer.grades2[course] = [grade]
        else:
            return 'Ошибка'
    def average_grades(self):
        list_grades = []
        for v in self.grades.values():
            for i in v:
                list_grades.append(i)
            res = round(sum(list_grades) / len(list_grades), 2)
            return res
    def __str__(self):
        res = f"Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за лекцию:{self.average_grades()} \nКурсы в процессе изучения:{','.join(self.courses_in_progress)} \nЗавершенные курсы:{','.join(self.finished_courses)}"
        return res
    def __lt__(self, other):
        return self.average_grades() < other.average_grades()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades2 = {}
    def average_grades2(self):
        list_grades2 = []
        for v in self.grades2.values():
            for i in v:
                list_grades2.append(i)
        res = round(sum(list_grades2) / len(list_grades2), 2)
        return res
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grades2()}'
        return res
    def __lt__(self, other):
        return self.average_grades2() < other.average_grades2()



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res


def average_grades_student(student_list, courses):
    sum_number = 0
    sum_grades = 0
    for s in student_list:
         if courses in s.grades:
            sum_number += len(s.grades[courses])
            sum_grades += sum(s.grades[courses])
    res = round((sum_grades / sum_number), 2)
    return res

def average_grades_lecturer(lecturer_list, courses):
    sum_number = 0
    sum_grades = 0
    for l in lecturer_list:
        if courses in l.grades2:
            sum_number += len(l.grades2[courses])
            sum_grades += sum(l.grades2[courses])
    res = round((sum_grades / sum_number), 2)
    return res




some_student = Student('Ruoy', 'Eman', 'm')
best_student = Student('Jeck', 'Yrle', 'm')
some_student.courses_in_progress += ['Python', 'C#']
best_student.courses_in_progress +=['Python', 'C#']
some_student.finished_courses += ['Git', '1С']
best_student.finished_courses += ['Git', '1С']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'C#']
best_reviewer = Reviewer('Niko', 'Akin')
best_reviewer.courses_attached += ['C#']

some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(best_student, 'Python', 9)
best_reviewer.rate_hw(some_student, 'C#', 5)
best_reviewer.rate_hw(best_student, 'C#', 8)
print(some_student.grades)
print(best_student.grades)

some_lecturer = Lecturer("Tom", "Ivanov")
some_lecturer.courses_attached += ['Python', 'C#']
best_lecturer = Lecturer('Vladimir', 'Rethyl')
best_lecturer.courses_attached += ['Python', 'C#']

some_student.rate_lect(some_lecturer, 'Python', 7)
some_student.rate_lect(best_lecturer, 'Python', 10)
some_student.rate_lect(some_lecturer, 'C#', 8)
some_student.rate_lect(best_lecturer, 'C#', 10)
print(some_lecturer.grades2)
print(best_lecturer.grades2)

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(some_student, '\n')

print(best_reviewer, '\n')
print(best_lecturer, '\n')
print(best_student, '\n')

print(some_student < best_student)
print(some_lecturer < best_lecturer)

students_list = [best_student, some_student]
lecturers_list = [best_lecturer, some_lecturer]

print(average_grades_student(students_list, 'Python'))
print(average_grades_lecturer(lecturers_list, 'Python'))