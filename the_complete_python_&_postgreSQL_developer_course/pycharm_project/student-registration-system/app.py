student_list = []


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
    for i, student in enumerate(students):
        print('ID: {}'.format(i))
        print_student_details(student)


def menu():
    selection = input(
        'Enter \'p\' to print the student list,'
        ' \'s\' to add a new student,'
        ' \'a\' to add a mark to a student,'
        ' or \'q\' to quit.'
        ' Enter your selection: ')

    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input('Enter the student ID to add a mark to: '))
            new_mark = int(input('Enter the new mark to be added: '))
            add_mark(student_list[student_id], new_mark)

        selection = input(
            'Enter \'p\' to print the student list,'
            ' \'s\' to add a new student,'
            ' \'a\' to add a mark to a student,'
            ' or \'q\' to quit.'
            ' Enter your selection: ')


menu()
