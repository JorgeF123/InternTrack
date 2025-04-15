ADD_INTERNSHIP = 1
VIEW_ALL_APPLICATIONS = 2
UPDATE_APPLICATIONS = 3
DELETE_APPLICATION = 4
EXIT = 5

applications = []



def main():
    choice = 0

    while choice != EXIT:

        try:

            choice = show_menu()
            if choice == ADD_INTERNSHIP:
                add_application()
            elif choice == VIEW_ALL_APPLICATIONS:
                view_applications()
            elif choice == UPDATE_APPLICATIONS:
                update_status()
            elif choice == DELETE_APPLICATION:
                delete_application()
            elif choice == EXIT:
                print('Program over goodbye...')

        except ValueError:
            print('Invalid input. Please enter a number.')
        except IndexError:
            print('Invalid index. Please choose a number from the list.')





def show_menu():
    print('1. Add Internship Application')
    print('2. View All Applications')
    print('3. Update Application Status')
    print('4. Delete Application')
    print('5. Exit')
    choice = int(input('Enter your choice '))
    return choice



def add_application():
    company_name = input('Enter company name ')
    role_title = input('Enter role title ')
    date_applied = input('Enter date you Applied ')
    status = 'Applied'

    application = {
        'company': company_name,
        'role': role_title,
        'date': date_applied,
        'status': status
    }
    applications.append(application)
    print('Application added!')



def view_applications():
    if not applications:
        print('No applications found.')

    else:
        for i,application in enumerate(applications):
            print(f"{i + 1}. Company: {application['company']}, Role: {application['role']}, Date Applied: {application['date']},  Status: {application['status']}")



def update_status():
    view_applications()
    application_index = int(input('Enter application index ')) - 1
    if application_index < len(applications):
        new_status = input('enter new status')
        applications[application_index]['status'] = new_status
        print('Status updated!')
    else:
        print('Invalid index.')

def delete_application():
    view_applications()
    application_index = int(input('Enter application index ')) - 1
    if application_index < len(applications):
       del_app = applications[application_index]
       del applications[application_index]
       print(f"Deleted application for {del_app['company']}.")
    else:
        print('Invalid index.')

main()
