from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

person = handleCrud('person')

person_data_template = {
    'id_card': 'id_card',
    'last_name': 'last_name',
    'first_name': 'first_name',
    'birth': 'birth',
    'gender': 'gender',
    'adress': 'adress',
    'phone': 'phone'
}

person_new_data_template = {
    'id_card': 'new_id_card',
    'last_name': 'new_last_name',
    'first_name': 'new_first_name',
    'birth': 'new_birth',
    'gender': 'new_gender',
    'adress': 'new_adress',
    'phone': 'new_phone'
}

def person_insert_template():
    person.insert(person_data_template)

def person_insert(person_data):
    person.insert(person_data)

def person_selectAll():
    return person.selectAll()

def person_count():
    return person.count()

def person_select(person_data):
    return person.select(person_data)

def person_update(person_data, person_new_data):
    person.update(person_data, person_new_data)

def person_delete(person_data):
    person.delete(person_data)

def person_deleteAll():
    person.deleteAll()

if __name__ == '__main__':
    print("insert template")
    person_insert_template()
    print(person_selectAll())
    print(" ")

    print("select person_data")
    print(person_select(person_data_template))
    print(" ")

    print("update person_data")
    person_update(
        person_data_template,
        person_new_data_template
    )
    print(person_selectAll())
    print(" ")

    print("insert person_data")
    person_insert(person_data_template)
    print(person_selectAll())
    print(" ")

    print("Counting person")
    print(f"Number of person : {person_count()}")
    print(" ")

    print("delete person_data")
    person_delete(person_data_template)
    print(person_selectAll())
    print(" ")

    print("delete all")
    person_deleteAll()
    print(person_selectAll())