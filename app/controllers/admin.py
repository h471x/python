from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

admin = handleCrud('admin')

admin_data_template = {
    'id_card': 'id_card',
    'last_name': 'last_name',
    'first_name': 'first_name',
    'birth': 'birth',
    'gender': 'gender',
    'adress': 'adress',
    'phone': 'phone',
    'username': 'username',
    'password': 'password',
    'workstation': 'workstation'
}

admin_new_data_template = {
    'id_card': 'new_id_card',
    'last_name': 'new_last_name',
    'first_name': 'new_first_name',
    'birth': 'new_birth',
    'gender': 'new_gender',
    'adress': 'new_adress',
    'phone': 'new_phone',
    'username': 'new_username',
    'password': 'new_password',
    'workstation': 'new_workstation'
}

def admin_insert_template():
    admin.insert(admin_data_template)

def admin_insert(admin_data):
    admin.insert(admin_data)

def admin_selectAll():
    return admin.selectAll()

def admin_count():
    return admin.count()

def admin_select(admin_data):
    return admin.select(admin_data)

def admin_update(admin_data, admin_new_data):
    admin.update(admin_data, admin_new_data)

def admin_delete(admin_data):
    admin.delete(admin_data)

def admin_deleteAll():
    admin.deleteAll()

if __name__ == '__main__':
    print("insert template")
    admin_insert_template()
    print(admin_selectAll())
    print(" ")

    print("select admin_data")
    print(admin_select(admin_data_template))
    print(" ")

    print("update admin_data")
    admin_update(
        admin_data_template,
        admin_new_data_template
    )
    print(admin_selectAll())
    print(" ")

    print("insert admin_data")
    admin_insert(admin_data_template)
    print(admin_selectAll())
    print(" ")

    print("Counting admin")
    print(f"Number of admin : {admin_count()}")
    print(" ")

    print("delete admin_data")
    admin_delete(admin_data_template)
    print(admin_selectAll())
    print(" ")

    print("delete all")
    admin_deleteAll()
    print(admin_selectAll())
