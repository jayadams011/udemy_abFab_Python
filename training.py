""" 
allow initial entry of employees.  
employee name
employee number
pay grade 

add new employee
edit employee 
delete employee 
print list of all employees
calculate payroll for all employees
"""

pay_grades={'a1':10.95,'b2':8.95,'c3':7.75,'d4':6.65} #establishes a "dict" of key pairs.

employee_data=[]

employee_numbers=set() #for testing for employee numbers

while(1):
    employee_number = input('enter an employee number -->')
    employee_name = input('enter an employee name -->')
    pay_grade = input('enter employee grade (a1,b2,c3,d4) -->')

    #test for employee number and name to have values
    if not(employee_number):
        print('You didn\'t enter an employee number.  Please reenter data. \n\n')
        continue

    if not(employee_name):
        print('You didn\'t enter an employee name.  Please reenter data. \n\n')
        continue

    # make sure pay grade is valid. 
    if not (pay_grades.get(pay_grade)):
        print('Sorry... you entered an invalid pay grade.  Please reenter all data\n\n')
        continue

    # test ti see if employee is in set and if so, have a user reenter data
    if employee_number in employee_numbers:
        print ('Employee number ', employee_number, 'is already used.  Please reenter data. \n\n')
        continue
    else:
        employee_numbers.add(employee_number)

    done = input('Enter X if this is the last employee entry or hit Enter to enter the next employee -->')






