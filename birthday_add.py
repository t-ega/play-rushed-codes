user_list = {}
from month_converter import month_converter


def add():
    celebrant = input('Please name of the celebrant you wish to add')
    celebrant_birthdate = input('Please date of celebrant in mm/dd/yyyy')
    month_converter(celebrant_birthdate)
    user_list.update({celebrant: celebrant_birthdate})
    if celebrant:
        print('Upload succcessful!')
    else:
        print('Not succesful!')


def look_up():
    celebrant_birthdate = input('Person date you want to lookup')
    if celebrant_birthdate in user_list:
        print(month_converter(user_list[celebrant_birthdate]))
    else:
        print('No such user!')


def update():
    celebrant_birthdate = input('Person date you want to change')
    if celebrant_birthdate in user_list:
        celebrant_birthdate_updated = input(f'Change {celebrant_birthdate} from {user_list[celebrant_birthdate]} to what?')
        update = user_list.update({celebrant_birthdate: celebrant_birthdate_updated})
        update = True
    else:
        print('User doesnt exist!')
    if update:
        print('Update Successful!')
    else:
        print('Not Succesful!')


def delete():
    print("Celebrant's birthday you wish to delete")
    celebrant_birthdate = input()
    choice = input(
        f'Are you sure you wish to delete {celebrant_birthdate} -{user_list[celebrant_birthdate]}? "Yes or No"')
    if choice.lower() == 'yes':
        del user_list[celebrant_birthdate]
        print('Deletion succesful!')
    else:
        print('Birthday not deleted')












