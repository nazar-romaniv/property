import auth
from main import Agent


class ApplicationSession:

    def __init__(self):
        self.user = None
        self.authenticator = auth.authenticator
        self.authorizer = auth.authorizer
        self.actions = {
            'find property': Agent.add_property,
            'display properties': Agent.display_properties,
            'add a property': Agent.add_property,
            'add a user':  auth.Authenticator.add_user,
            'delete a user': auth.Authenticator.del_user,
            'manage permissions': auth.Authorizer.give_permission
        }
        print('Welcome!')
        while len(self.authenticator.users.keys()) == 0:
            print('Create a new user profile')
            self.add_user(None)
        self.log_in()

    def log_in(self):
        while self.user is None:
            username = input('Enter username: ')
            password = input('Enter password: ')
            try:
                self.authenticator.log_in(username, password)
            except auth.DoesNotExist:
                print('User does not exist!')
            except auth.InvalidPassword:
                print('Wrong password!')
            except auth.AlreadyLoggedIn:
                print('You are already logged in!')
            else:
                print('Welcome, {}!'.format(username))
                self.user = self.authenticator.users[username]

    def add_user(self, username):
        while True:
            try:
                if self.authorizer.verify_permission('add a user', username):
                    new_username = input('Enter a new username: ')
                    password = input('Enter the new user\'s password: ')
                    self.authenticator.add_user(new_username, password)
            except auth.AlreadyExists:
                print('Username already exists!')
            except auth.PasswordTooShort:
                print('Password is too short!')
            except auth.PermissionDenied:
                print('You do not have the permission to add user entries!')
                raise
            except auth.DoesNotExist:          #this will be the case for the creation of the very first user account
                new_username = input('Enter a new username')
                password = input('Enter the new user\'s password')
                self.authenticator.add_user(new_username, password)
                for permission in self.authorizer.permissions:
                    self.authorizer.give_permission(permission, new_username)
            except KeyboardInterrupt:
                break
            else:
                break
            print('Press Ctrl+C to exit')

    def manage_permissions(self, username):
        while True:
            try:
                if self.authorizer.verify_permission('manage permissions', username)
                    actions = {
                        'add a permission': auth.Authorizer.add_permission,
                        'withdraw a permission': auth.Authorizer.withdraw_permission,
                        'list permissions': auth.Authorizer.list_permissions,
                        'give permission': auth.Authorizer.give_permission
                    }
                    while True:
                        print('Enter the user whose permissions you want to edit: ')
                        self.authenticator.list_users()
                        user_to_edit = ''
                        while user_to_edit not in self.authenticator.users.keys():
                            username = input()

            except auth.PermissionDenied:
                print('You are not allowed to manage permissions!')
                break
