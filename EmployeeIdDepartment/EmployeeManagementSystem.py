# Import necessary libraries
import pickle
from EmployeeIdDepartment import Employee


# STEP 1 = DEFINE FUNCTIONS FOR EACH CHOICE

# Lookup an employee
def lookup(dictionary):
    # Look up the ID number if it is in the dictionary
    ID = int(input('Enter the employee ID number: '))
    if ID in dictionary.keys():
        print(ID, ': ', dictionary[ID])
        print(dictionary.get(ID))
    else:
        print("That ID number was not found.")

    # Offer the user the menu of choices again from main()
    proceed = True
    return proceed


# Add an employee
def add(dictionary):
    # Add a new employee
    ID = int(input('Enter the employee ID number: '))
    name = input('Enter the name of the employee: ')
    dept = input('Enter the employee department: ')
    job = input('Enter the employee job title: ')

    entry = Employee.Employee(ID, name, dept, job)
    dictionary[ID] = entry
    print('Employee added succesfully')

    # Offer the user the menu of choices again from main()
    proceed = True
    return proceed


# Change an employee
def change(dictionary):
    # If user-entered ID is in dictionary, allow them to change the info
    ID = input('Enter the employee ID you would like to change: ')
    if ID in dictionary.keys():
        name = input('Enter new employee name: ')
        newId = input('Enter new employee ID: ')
        dept = input('Enter new employee department: ')
        job = input('Enter new employee job title: ')
        entry = Employee.Employee(newID, name, dept, job)
        dictionary[ID] = entry
        print('Employee changed successfully.')
    else:
        print('That employee ID was not found.')

    # Offer the user the menu of choices again from main()
    proceed = True
    return proceed


# Delete an employee
def delete(dictionary):
    # If user-entered ID is in dictionary, delete the entry
    ID = input('Enter the employee ID you would like to remove: ')
    if ID in dictionary.keys():
        del dictionary[ID]
        print('Employee removed successfully')
    else:
        print('That employe ID was not found.')

    # Offer the user the menu of choices again from main()
    proceed = True
    return proceed


# Save the dictionary and quit the program
def save_quit(dictionary):
    # Pickle the dictionary and save to a file
    output_file = open('employee_data.dat', 'wb')
    pickle.dump(dictionary, output_file)
    output_file.close

    # End the while loop in main() so program quits
    proceed = False
    return proceed


# STEP 2 - Main Function
def main():
    # Try to open the existing dictionary file
    try:
        input_file = open('employee_data.dat', 'rb')
        employee_dictionary = pickle.load(input_file)
        input_file.close()

    # If no such file exists, create a new dictionary
    except:
        employee_dictionary = {}

    # While loop to continue until user chooses to quit
    proceed = True
    while proceed:
        # Display user's option menu and ask for a choice
        print('\n Employee Management System\n')
        print('\t1. Lookup an employee')
        print('\t2. Add a new employee')
        print('\t3. Change an existing employee')
        print('\t4. Delete an existing employee')
        print('\t5. Save and Quit\n')

        option_choice = int(input('Enter an option to continue: '))

        # Map each choice to the functions below using a dictionary
        options = {1: lookup, 2: add, 3: change, 4: delete, 5: save_quit, }
        proceed = options[option_choice](employee_dictionary)
