basic_dic = {'name': 'steven', 'age': 37}
print(basic_dic['name'])

student = [{'name': 'steven', 'age': 37, 'hobbies': ['movie', 'music'], 'exams': {
    'final': 99,
    'midterm': 100
}}]
print(student[0]['name'])
print(student[0]['hobbies'][0])
print(student[0]['exams']['final'])
