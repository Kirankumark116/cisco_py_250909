import repo
# test create employee and read all
employee=(101, 'banu', 22, 50000, True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully.')
print('after add:',repo.read_all_employee())

employee=(102, 'mahesh', 46, 4000.50, True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully.')
print('after add:',repo.read_all_employee())

employee=(103, 'Vaishnavi', 21, 40000.75, True)
repo.create_employee(employee)
print(f'Employee {employee[1]} created successfully.')
print('after add:',repo.read_all_employee())

#test read by id
employee=repo.read_by_id(103)
if employee==None:
    print("employuee not found")
else:
    print(employee)

#test update
employee=repo.read_by_id(103)
if employee == None:
    print('employee not found')
else:
    id, name, age, salary, is_sctive=employee
    salary+=20000
    new_employee=(id, name, age, salary, is_sctive)
    repo.update(103,)