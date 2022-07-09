class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lection(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _av_grade(self):
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        result = sum(new_list) / len(new_list)
        self.avg_grade = result
        return result

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._av_grade()}' \
              f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
              f'\nЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._avg_grade()}'
        return res

    def _avg_grade(self):
        new_list = []
        for grade in self.grades.values():
            new_list.extend(grade)
        result = sum(new_list) / len(new_list)
        self.avg_grade = result
        return result

    def __lt__(self, other):

        if not isinstance(other, Lector):
            print('Можно сравнивать только Лекторов!')
            return
        elif self.average_grade_of_lector() > other.average_grade_of_lector():
            return f'\n{self.name} {self.surname} имеет среднюю оценку за лекции выше чем {other.name} {other.surname}'
        else:
            return f'\n{other.name} {other.surname} имеет среднюю оценку за лекции выше чем {self.name} {self.surname}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Roy', 'Erman', 'male')
best_student.courses_in_progress += ['Python']
nice_student = Student('Vladimir', 'Ivanov', 'male')
nice_student.courses_in_progress += ['Git', 'Python']


Nice_reviewer = Reviewer('Ivan', 'Ivanov')
Nice_reviewer.courses_attached += ['Python']
Nice_reviewer.rate_hw(best_student, ['Python'], 9)
Nice_reviewer.rate_hw(nice_student, ['Git'], 8)

Nice_lector = Lector('Alexandr', "Alexandrov")
Good_lector = Lector('Andrey', 'Andreyev')
best_student.rate_lection(Nice_lector, 'Python', 10)
nice_student.rate_lection(Good_lector, 'Python', 9)

students = [best_student, nice_student]
lectors = [Nice_lector, Good_lector]

def av_students(students):
    new_list = []
    for student in students:
        for grade in student.grades:
            new_list.extend(grade)
    result = sum(new_list) / len(new_list)
    self.avg_grade = result
    return result

def av_lectors(lectors):
    new_list = []
    for lector in lectors:
        for grade in lector.grades:
            new_list.extend(grade)
    result = sum(new_list) / len(new_list)
    self.avg_grade = result
    return result

students_avg = av_students(students)
lectors_avg = av_lectors(lectors)

print(Nice_reviewer)
print(best_student)

