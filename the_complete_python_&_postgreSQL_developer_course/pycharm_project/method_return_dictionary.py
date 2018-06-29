def create_student():
    name = input('Please enter the new student\'s name:')
    student_data = {
        'name': name,
        'mark': []
    }

    return student_data


print(create_student())
