from classes import Student, Course


def add_new_student(students_list):
    name = input('enter student name')
    class_number = input('enter student class')
    new_student = Student(name, class_number, [])
    students_list.append(new_student)
    print(new_student.get_student_details())
    print('student added successfully')


def find_student(student_num, students_list):
    student_data = [ele for ele in students_list if ele.student_number == student_num]
    if not len(student_data):
        return False
    return student_data[0]


def find_course(course_name, course_list):
    course = [ele for ele in course_list if ele.course_name == course_name]
    if not len(course):
        return False
    return course[0]


def remove_student(students_list):
    number = float(input('enter student id'))
    for i in range(len(students_list)):
        if students_list[i].student_number == number:
            del students_list[i]
            print('student deleted')
            break
        elif i == len(students_list) - 1 and not students_list[i].student_number == number:
            print('student does not exist')


def edit_student(students_list):
    number = float(input('enter student id'))
    student = find_student(number, students_list)
    if not student:
        print('student does not exist')
        return
    name = input('enter new name: ')
    student_class = input('enter new class: ')
    student.edit_student(name, student_class)
    print(student.get_student_details())
    print('student edited successfully')


def display_all_students(students_list):
    if not len(students_list):
        print('there is no students yet')
        return
    for i in students_list:
        print(i.get_student_details())


def add_new_course(course_list):
    course_name = input('enter course name')
    course_class = input('enter course class')
    new_course = Course(course_name, course_class)
    course_list.append(new_course)
    print(new_course.course_name, new_course.course_class)
    print('course saved successfully')


def add_course_to_student(students_list, course_list):
    student_id = float(input('enter student id'))
    student = find_student(student_id, students_list)
    if not student:
        print('student does not exist')
        return
    course_name = input('enter course name')
    course = find_course(course_name, course_list)
    if not course:
        print('course does not exist')
        return
    student.add_course(course)
    print('course added successfully')
