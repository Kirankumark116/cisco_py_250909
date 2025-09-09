employees=[]

employee=('banu', 22, 50000, True)
employees.append(employee)

employee=('mahesh', 46, 4000.50, True)
employees.append(employee)

employee=('Vaishnavi', 21, 40000.75, True)
employees.append(employee)

print('after add alla employee:',employees)

I=0
search='Vaishnavi'
index=-1
for emp in employees:
    if emp[0] == search:
        index=I
        break
    I+=1

if index == -1:
    print("Employee not found")
else:
    search_employee=employees[index]
    print(search_employee)
    salary = float(input('Salary:'))
    employee=(search_employee[0],search_employee[1],salary,search_employee[3])
print('after search and update:', employees)

employee=('Dravid',50, 200.75, True)
employees.append(employee)
print('after add Dravid:',employees)
employees.pop()
print('after delete Dravid:',employees)

position=1
employees.pop(position)
print('after delete Mahesh:',employees)