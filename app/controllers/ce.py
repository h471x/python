from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from classes.database.dbcrud import CrudHandler as handleCrud

ce = handleCrud('ce')

ce_data_template = {
    'cename': 'cename',
    'ue': 'ue'
}

ce_new_data_template = {
    'cename': 'new_cename',
    'ue': 'new_ue'
}

def ce_insert_template():
    ce.insert(ce_data_template)

def ce_insert(ce_data):
    ce.insert(ce_data)

def ce_selectAll():
    return ce.selectAll()

def ce_count():
    return ce.count()

def ce_select(ce_data):
    return ce.select(ce_data)

def ce_update(ce_data, ce_new_data):
    ce.update(ce_data, ce_new_data)

def ce_delete(ce_data):
    ce.delete(ce_data)

def ce_deleteAll():
    ce.deleteAll()

if __name__ == '__main__':
    print("insert template")
    ce_insert_template()
    print(ce_selectAll())
    print(" ")

    print("select ce_data")
    print(ce_select(ce_data_template))
    print(" ")

    print("update ce_data")
    ce_update(
        ce_data_template,
        ce_new_data_template
    )
    print(ce_selectAll())
    print(" ")

    print("insert ce_data")
    ce_insert(ce_data_template)
    print(ce_selectAll())
    print(" ")

    print("Counting ce")
    print(f"Number of ce : {ce_count()}")
    print(" ")

    print("delete ce_data")
    ce_delete(ce_data_template)
    print(ce_selectAll())
    print(" ")

    print("delete all")
    ce_deleteAll()
    print(ce_selectAll())