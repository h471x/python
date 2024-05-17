from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

student = handleCrud('student')

student_data_template = {
    'id_card': 'id_card',
    'last_name': 'last_name',
    'first_name': 'first_name',
    'birth': 'birth',
    'gender': 'gender',
    'adress': 'adress',
    'phone': 'phone',
    'student_id': 'student_id',
    'major': 'major',
    'Grade': 'Grade',
    'cursus': 'cursus'
}

student_new_data_template = {
    'id_card': 'new_id_card',
    'last_name': 'new_last_name',
    'first_name': 'new_first_name',
    'birth': 'new_birth',
    'gender': 'new_gender',
    'adress': 'new_adress',
    'phone': 'new_phone',
    'student_id': 'new_student_id',
    'major': 'new_major',
    'Grade': 'new_Grade',
    'cursus': 'new_cursus'
}

def student_insert_template():
    student.insert(student_data_template)

def student_insert(student_data):
    student.insert(student_data)

def student_selectAll():
    return student.selectAll()

def student_count():
    return student.count()

def student_select(student_data):
    return student.select(student_data)

def student_update(student_data, student_new_data):
    student.update(student_data, student_new_data)

def student_delete(student_data):
    student.delete(student_data)

def student_deleteAll():
    student.deleteAll()

if __name__ == '__main__':
    print("insert template")
    student_insert_template()
    print(student_selectAll())
    print(" ")

    print("select student_data")
    print(student_select(student_data_template))
    print(" ")

    print("update student_data")
    student_update(
        student_data_template,
        student_new_data_template
    )
    print(student_selectAll())
    print(" ")

    print("insert student_data")
    student_insert(student_data_template)
    print(student_selectAll())
    print(" ")

    print("Counting student")
    print(f"Number of student : {student_count()}")
    print(" ")

    print("delete student_data")
    student_delete(student_data_template)
    print(student_selectAll())
    print(" ")

    print("delete all")
    student_deleteAll()
    print(student_selectAll())
