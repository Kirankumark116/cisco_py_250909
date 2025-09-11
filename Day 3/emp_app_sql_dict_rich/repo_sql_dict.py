#CRUD (Create, Read All | Read One, Update, Delete)

from db_setup import session, Employee
from log import logging
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from exc import EmployeeNotFoundError,EmployeeAlreadyExistError, DatabaseError
def create_employee(employee):
    try:
        employee_model= Employee(
            id = employee['id'],
            name = employee['name'],
            age = employee['age'],
            salary = employee['salary'],
            is_active= employee['is_active'])
        session.add(employee_model) #insert Stmt db
        session.commit()
        logging.info("employee created")
    except IntegrityError as ex:
        session.rollback()
        logging.error("Duplicate employee id:%s",ex)
        raise EmployeeAlreadyExistError(f"Employee id={employee['id']} exists already.")
    except SQLAlchemyError as ex:
        session.rollback()
        logging.error("Database error in creating employee:%s",ex)
        raise DatabaseError("Error in creating employee.")

def read_all_employee():
    employees=session.query(Employee).all()
    dict_employees=[]
    for employee in employees:
        employee_dict={'id': employee.id,'name':employee.name,'age':employee.age,'salary':employee.salary,
                       'is_active':employee.is_active}
        dict_employees.append(employee_dict)
    logging.info("all records are read")
    return dict_employees 

def read_model_by_id(id):
    employee = session.query(Employee).filter_by(id=id).first()
    logging.info("employee read by the ID")
    return employee

def read_by_id(id):
    employee = read_model_by_id(id)
    if not employee:
        logging.info("employee not found")
        return None
    employee_dict = {'id':employee.id,'name':employee.name,
                     'age':employee.age,'salary':employee.salary,
                     'is_active':employee.is_active}
    logging.info("employee read by ID")
    return employee_dict

def update(id, new_employee):#new_employee is update at id
    employee = read_model_by_id(id)
    if not employee:
        logging.info("employee not found")
        return
    employee.salary = new_employee['salary']
    session.commit()
    
def delete_employee(id):
    employee = read_model_by_id(id)
    if not employee:
        return
    session.delete(employee)
    session.commit()
