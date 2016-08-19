'''
Facebook implemented in Python!
'''

# A dictionary to hold all users in application memory.
# Each entry in the users database is keyed with the email address of
# the user (as it must be unique) and the value is a dictionary of the
# user object itself.
users_db = {}


def register_user():
    '''
    Registers a new user into the users database
    '''
    pass

def login():
    '''
    Attempts to log in an existing user
    '''
    pass

def pre_login_menu():
    '''
    Menu that all users see
    '''
    while True:
        print('1. Log in')
        print('2. Register')
        print('3. Quit')
        selection = raw_input('Selection: ')

        if selection == '1':
            login()
        elif selection == '2':
            register_user()
        elif selection == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid selection, please try again')


def post_login_menu():
    '''
    Menu that only logged-in users can see
    '''
    while True:
        # Nothing to do here yet!
        print('1. Log out')
        selection = raw_input('Selection: ')

        if selection == '1':
            print('Logging out')
            break
        else:
            print('Invalid selection, please try again')


def main():
    '''
    The main program entry point
    '''
    pass


if __name__ == '__main__':
    main()
