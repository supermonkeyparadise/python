student_list=[]

def create_student():
    name = input('Please enter the new student\'s name:')
    student_data = {
        'name': name,
        'mark': []
    }

    return student_data


def add_mark(student, mark):
    student['mark'].append(mark)
    return None


def calculate_average_mark(student):
    number = len(student['mark'])

    if number == 0:
        return 0

    total = sum(student['mark'])

    return total / number


def print_student_details(student):
    print('{}, average mark: {}.'.format(student['name'], calculate_average_mark(student)))


def print_student_list(students):
    for student in students:
        print_student_details(student)


s = create_student()

add_mark(s, 5)
add_mark(s, 7)

print(calculate_average_mark(s))
