# the list "students" is already defined
print([student[0] for student in students if student[1] == 'A'])

"""
or:
[name for name, grade in students if grade == 'A']
"""
