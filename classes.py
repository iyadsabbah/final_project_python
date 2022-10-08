import random


class Course:
    course_id = ''
    course_name = ''
    course_class = ''

    def __init__(self, course_name, course_class):
        self.course_name = course_name
        self.course_class = course_class
        self.course_id = random.random()


class Student:
    student_name = ''
    student_number = 0
    student_class = ''
    courses = []

    def __init__(self, student_name, student_class, courses):
        self.student_name = student_name
        self.student_number = random.random()
        self.student_class = student_class
        self.courses = courses

    def add_course(self, course):
        if course.course_class == self.student_class:
            self.courses.append(course)
        else:
            return

    def get_student_details(self):
        return {
            'student_name': self.student_name,
            'student_class': self.student_class,
            'courses': [c.course_name for c in self.courses],
            'id': self.student_number
        }

    def edit_student(self, student_name, student_class):
        self.student_name = student_name
        self.student_class = student_class
