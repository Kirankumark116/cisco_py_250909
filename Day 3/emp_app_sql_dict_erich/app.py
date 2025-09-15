'''application'''
from db import repo_sql_dict as repo

def create():

    """
    create function
    """
    emp_id = int(input('ID:'))
    name = input('Name:')
    age = int(input('Age:'))
    salary = float(input('Salary:'))
    is_active = input('Active(y/n):').upper() == 'Y'
    employee = {'id':emp_id, 'name':name, 'age':age,
                'salary':salary, 'is_active':is_active}
    try:
        repo.create_employee(employee)
        print('Employee Created Successfully.')
    except repo.IntegrityError as ex:
        print(f"Dupilcate employee id:{ex}")
    except repo.SQLAlchemyError as ex:
        print(f"Database error in creating employee:{ex}")

def read_all():
    '''read_all'''
    print('List of Employees:')
    for employee in repo.read_all_employee():
        print(employee)

def read_by_id():
    '''read_by_id'''
    emp_id = int(input('ID:'))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee not found.')
    else:
        print(employee)

def update():
    '''update'''
    emp_id = int(input('ID:'))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee Not Found')
    else:
        print(employee)
        salary = float(input('New Salary:'))
        new_employee = {'id':employee['id'],
            'name':employee['name'],
            'age':employee['age'], 
            'salary':salary, 
            'is_active':employee['is_active']}
        repo.update(emp_id, new_employee)
        print('Employee updated successfully.')

def delete():
    '''delete'''
    emp_id = int(input('ID:'))
    employee = repo.read_by_id(emp_id)
    if employee is None:
        print('Employee Not Found')
    else:
        repo.delete_employee(emp_id)
        print('Employee Deleted Succesfully.')

def menu():
    '''menu'''
    message = '''
Options are:
1 - Create Employee
2 - List All Employees
3 - Read Employee By Id
4 - Update Employee
5 - Delete Employee
6 - Exit 
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        create()
    elif choice == 2:
        read_all()
    elif choice == 3:
        read_by_id()
    elif choice == 4:
        update()
    elif choice == 5:
        delete()
    elif choice == 6:
        print('Thankyou for using Application')
    return choice

def menus():
    '''menu'''
    choice = menu()
    while choice != 6:
        choice = menu()
if __name__ == "__main__":
    menus()