from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

teacher = handleCrud('teacher')

teacher_data_template = {
    'id_card': 'id_card',
    'last_name': 'last_name',
    'first_name': 'first_name',
    'birth': 'birth',
    'gender': 'gender',
    'adress': 'adress',
    'phone': 'phone',
    'teacher_id': 'teacher_id'
}

teacher_new_data_template = {
    'id_card': 'new_id_card',
    'last_name': 'new_last_name',
    'first_name': 'new_first_name',
    'birth': 'new_birth',
    'gender': 'new_gender',
    'adress': 'new_adress',
    'phone': 'new_phone',
    'teacher_id': 'new_teacher_id'
}

def teacher_insert_template():
    teacher.insert(teacher_data_template)

def teacher_insert(teacher_data):
    teacher.insert(teacher_data)

def teacher_selectAll():
    return teacher.selectAll()

def teacher_count():
    return teacher.count()

def teacher_select(teacher_data):
    return teacher.select(teacher_data)

def teacher_update(teacher_data, teacher_new_data):
    teacher.update(teacher_data, teacher_new_data)

def teacher_delete(teacher_data):
    teacher.delete(teacher_data)

def teacher_deleteAll():
    teacher.deleteAll()

if __name__ == '__main__':
    print("insert template")
    teacher_insert_template()
    print(teacher_selectAll())
    print(" ")

    print("select teacher_data")
    print(teacher_select(teacher_data_template))
    print(" ")

    print("update teacher_data")
    teacher_update(
        teacher_data_template,
        teacher_new_data_template
    )
    print(teacher_selectAll())
    print(" ")

    print("insert teacher_data")
    teacher_insert(teacher_data_template)
    print(teacher_selectAll())
    print(" ")

    print("Counting teacher")
    print(f"Number of teacher : {teacher_count()}")
    print(" ")

    print("delete teacher_data")
    teacher_delete(teacher_data_template)
    print(teacher_selectAll())
    print(" ")

    print("delete all")
    teacher_deleteAll()
    print(teacher_selectAll())