class Student:
    def __init__(self, name, surname, gender, sum_grades=0, number_of_ratings=0):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.number_of_ratings = number_of_ratings
        self.sum_grades = sum_grades
        self.grades = {}
    def rate_lec(self, lecturer, course, grade_lec):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.sum_grades += grade_lec
            lecturer.number_of_ratings += 1
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade_lec]
            else:
                lecturer.lecture_grades[course] = [grade_lec]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f"Имя: {self.name} " \
              f"\nФамилия: {self.surname} " \
              f"\nСредняя оценка за домашние задания: {round(self.sum_grades / self.number_of_ratings, 1)}" \
              f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress) } " \
              f"\nЗавершенные курсы: {', '.join(self.finished_courses) }"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Их нельзя сравнивать!')
            return
        else:
            sum_self = self.sum_grades / self.number_of_ratings
            sum_other = other.sum_grades / other.number_of_ratings
        return sum_self < sum_other

class Mentor:
    def __init__(self, name, surname, sum_grades=0, number_of_ratings=0):
        self.name = name
        self.surname = surname
        self.sum_grades = sum_grades
        self.number_of_ratings = number_of_ratings
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}
    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname} \n {round(self.sum_grades / self.number_of_ratings, 1)}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Их нельзя сравнивать!')
            return
        else:
            sum_self = self.sum_grades / self.number_of_ratings
            sum_other = other.sum_grades / other.number_of_ratings
        return sum_self > sum_other

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.sum_grades += grade
            student.number_of_ratings += 1
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f"Имя: {self.name} \nФамилия: {self.surname}"
        return res



# Определение объектов и их атрибутов

lecturer = Lecturer('Учитель', 'Сплинтер')
lecturer.courses_attached += ['Python', "Java"]

lecturer2 = Lecturer('Магистр', 'Йода')
lecturer2.courses_attached += ['Python',"Paskal"]

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ["Fortran"]

best_student2 = Student('Vasiliy', 'Terkin', 'male')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Logo']
best_student2.finished_courses += ["Fortran"]

cool_reviever = Reviewer('Gendalf', 'Gray')
cool_reviever.courses_attached += ['Python']

cool_reviever2 = Reviewer('Gendalf', 'Gray')
cool_reviever2.courses_attached += ['Python', 'Logo']



# Полевые испытания



best_student2.rate_lec(lecturer,'Python', 5)
best_student2.rate_lec(lecturer,'Python', 10)

cool_reviever2.rate_hw(best_student, 'Python', 10)
cool_reviever2.rate_hw(best_student, 'Python', 7)
cool_reviever2.rate_hw(best_student, 'Python', 8)

cool_reviever.rate_hw(best_student, 'Python', 10)
cool_reviever.rate_hw(best_student2, 'Python', 3)
cool_reviever.rate_hw(best_student2, 'Python', 10)

best_student.rate_lec(lecturer,'Python', 5)
best_student.rate_lec(lecturer,'Python', 6)
best_student.rate_lec(lecturer2,'Python', 10)
best_student.rate_lec(lecturer2,'Python', 6)
best_student.rate_lec(lecturer,'Python', 5)
best_student.rate_lec(lecturer2,'Python', 6)

list_student = [best_student, best_student2]
list_lecturer = [lecturer, lecturer2]


def average_rating (list_student, course):
    list_rating_oncourse = []
    for student in list_student:                   # проверить наличие курса в progress_course
        list_rating_oncourse += student.grades[course]
    sum_average_rating = sum(list_rating_oncourse) / len(list_rating_oncourse)
    return sum_average_rating

def average_rating_lec (list_lecturer, course):
    list_rating_lec = []                             # проверить наличие курса в attache_course
    for lecturer in list_lecturer:
        list_rating_lec += lecturer.lecture_grades[course]
    sum_average_rating_lec = sum(list_rating_lec) / len(list_rating_lec)
    return sum_average_rating_lec



print(f"\nДанные  студента--------    \n{best_student2} \n------------------------")

print(f"\nДанные проверяещего--------    \n{cool_reviever} \n------------------------")

print(f"\nДанные лектора---------     \n{lecturer} \n------------------------")

print( f" \nРезультат сравнения лекторов --> {lecturer > lecturer2} \n------------------------")

print(f" \nРезультат сравнения студентов --> {best_student > best_student2} \n------------------------")

print(round(average_rating(list_student, 'Python'),1))
print(round(average_rating_lec(list_lecturer, "Python"), 1))