from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

have = handleCrud('have')

have_data_template = {
    '--': '--',
    '--': '--',
    '--': '--',
    'rf_cename)': 'rf_cename)'
}

have_new_data_template = {
    '--': 'new_--',
    '--': 'new_--',
    '--': 'new_--',
    'rf_cename)': 'new_rf_cename)'
}

def have_insert_template():
    have.insert(have_data_template)

def have_insert(have_data):
    have.insert(have_data)

def have_selectAll():
    return have.selectAll()

def have_count():
    return have.count()

def have_select(have_data):
    return have.select(have_data)

def have_update(have_data, have_new_data):
    have.update(have_data, have_new_data)

def have_delete(have_data):
    have.delete(have_data)

def have_deleteAll():
    have.deleteAll()

if __name__ == '__main__':
    print("insert template")
    have_insert_template()
    print(have_selectAll())
    print(" ")

    print("select have_data")
    print(have_select(have_data_template))
    print(" ")

    print("update have_data")
    have_update(
        have_data_template,
        have_new_data_template
    )
    print(have_selectAll())
    print(" ")

    print("insert have_data")
    have_insert(have_data_template)
    print(have_selectAll())
    print(" ")

    print("Counting have")
    print(f"Number of have : {have_count()}")
    print(" ")

    print("delete have_data")
    have_delete(have_data_template)
    print(have_selectAll())
    print(" ")

    print("delete all")
    have_deleteAll()
    print(have_selectAll())
