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

    # Strore data away
    employee_data.append([employee_number, employee_name, pay_grade])

    # See if it is time to exit the loop
    if ((done == 'x') or (done == 'X')):
        break 

    # Create main operation menu Loop

    while(1) :
        print('make a selection. \n')
        choice=input ('''Enter A to add a new emplyee
    Enter E to edit an existin employee
    Enter P to print a list of all employee data
    Enter D to remove an employee
    Enter C to calculate payroll
    Enter X to exit
    
    Enter Choice Here --> ''')

        # See if it is time to exit the loop
        if ((choice == 'x') or (choice == 'X')):
            break
        elif ((choice == "A") or (choice == 'a')):
            employee_number = input('Enter employee number -->')
            employee_name = input ('enter employee full name -->')
            pay_grade = input('enter employee grade (a1,b2,c3,d4) -->')

            # Be sure employee number and name have values
            if not(employee_number) :
                print ('You didn\'t enter an employee number.  Please reenter data. \n\n')
                continue

            if not(employee_name) :
                print ('You didn\'t enter an employee name.  Please reenter data. \n\n')

            if not(pay_grades.get(pay_grade)):
                print ('Sorry... you entered an invalid pay grade.  Please reenter all data\n\n')
                continue

            #test to see if employee number is in set and if so, have user reeenter data
            if employee_number in employee_numbers: 
                print('employee number ', employee_number, 'is already used.  Please reenter data. \n\n')

            else: 
                employee_numbers.add(employee_number)

            # Store data away
            employee_data.append([employee_number, employee_name, pay_grade])

        elif (( choice == 'E') or (choice == 'e')):
            employee_number = input ('enter employee number -->')
            employee_name = input ('enter employee full name -->')
            pay_grade = input('enter employee grade (a1,b2,c3,d4) -->')


            # Be sure employee number and name have values
            if not (employee_number):
                print ('You didn\'t enter an employee number.  Please reenter data. \n\n')
                continue

            if not (employee_name):
                print('You didn\'t enter an employee number.  Please reenter all data \n\n')
                continue

            # Make sure pay grade is valid
            if not (paygrades.get(pay_grade)):
                print('Sorry... you entered an invalid pay grade.  Please reenter all data\n\n')
                continue

            #test to see if employee number is in set and if so, save edits.  Otherwise notify employee doesn't exist
            if employee_number in employee_numbers:
                #find reocrd to update
                j = 0
                for i in employee_data:
                    if (employee_number == i[0]):
                        employee_data[j]= [employee_number, employee_name,pay_grade]
                        continue
                    j += 1

            else:
                print('employee number  ', employee_number, ' is not a valid employee.  Data not saved\n\n')


        elif ((choice == 'p') or (choice == 'P')):
            # Note: You could add to this to make nice rows but we haven't covered this yet. 
            for i in employee_data:
                print (i[0], i[1], i[2])

        elif ((choice == 'd') or (choice =='D')):
            employee_number = input('enter employee number --> ')

            # Be sure employee number and name have values
            if not (employee_number):
                print('You didn\'t enter an employee number.  Please reenter data. \n\n')
                continue

            # test to see if employee number is in set and if so, delete the record.
            # Otherwise notify emplyee doesnt exist

            









