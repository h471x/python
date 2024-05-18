from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handle_crud

student = handle_crud('student')

student_data_template = {
    'id_card': '0123456789',
    'last_name': 'Eliot',
    'first_name': 'Alderson',
    'birth': '2003-05-22',
    'gender': 'M',
    'adress': 'New Jersey',
    'phone': '0123456789',
    'student_id': '0006',
    'major': 'Computer Science',
    'level': 'M2',
    'cursus': 'Cybersecurity'
}

student_new_data_template = {
    'id_card': '0123456789',
    'last_name': 'Sam',
    'first_name': 'Sepiol',
    'birth': '2003-05-22',
    'gender': 'M',
    'adress': 'New Jersey',
    'phone': '0123456789',
    'student_id': '0006',
    'major': 'Computer Science',
    'level': 'M2',
    'cursus': 'Cybersecurity'
}

def student_insert_template():
    student.insert(student_data_template)

def student_insert(student_data):
    student.insert(student_data)

def student_select_all():
    return student.select_all()

def student_count():
    return student.count()

def student_select(student_data):
    return student.select(student_data)

def student_update(student_data, student_new_data):
    student.update(student_data, student_new_data)

def student_delete(student_data):
    student.delete(student_data)

def student_delete_all():
    student.delete_all()

if __name__ == '__main__':
    print("insert template")
    student_insert_template()
    print(student_select_all())
    print(" ")

    print("select student_data")
    print(student_select(student_data_template))
    print(" ")

    print("update student_data")
    student_update(
        student_data_template,
        student_new_data_template
    )
    print(student_select_all())
    print(" ")

    print("insert student_data")
    student_insert(student_data_template)
    print(student_select_all())
    print(" ")

    print("Counting student")
    print(f"Number of student : {student_count()}")
    print(" ")

    print("delete student_data")
    student_delete(student_data_template)
    print(student_select_all())
    print(" ")

    print("delete all")
    student_delete_all()
    print(student_select_all())
