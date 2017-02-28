import auth
from main import Agent


class ApplicationSession:

    def __init__(self):
        self.user = None
        self.authenticator = auth.authenticator
        self.authorizer = auth.authorizer
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
                if self.authorizer.verify_permission('add and delete users', username):
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
                if self.authorizer.verify_permission('manage permissions', username):
                    actions = {
                        '0': auth.Authorizer.add_permission,
                        '1': auth.Authorizer.withdraw_permission,
                        '2': auth.Authorizer.give_permission,
                        '3': auth.Authorizer.print_permissions
                    }
                    while True:
                        try:
                            print('Enter the user whose permissions you want to edit/view: (Press Ctrl+C to exit) ')
                            self.authenticator.list_users()
                            user_to_edit = ''
                            while user_to_edit not in self.authenticator.users.keys():
                                user_to_edit = input()
                            print('The permissions of {}'.format(user_to_edit),
                                  self.authorizer.list_permissions(user_to_edit))
                            print(
                                '''0 - add a permission
                                1 - withdraw a permission
                                2 - grant a permission
                                3 - print all available permissions'''
                            )
                            action = None
                            options = ('0', '1', '2', '3')
                            while action not in options:
                                action = input()
                            if action != '3':
                                print('Enter the permission name: ')
                                perm_name = ''
                                while perm_name not in self.authorizer.permissions.keys():
                                    perm_name = input()
                                if action == '0':
                                    actions[action](self.authorizer.actions, perm_name)
                                else:
                                    actions[action](self.authorizer.actions, perm_name, user_to_edit)
                            else:
                                self.authorizer.print_permissions()
                        except KeyboardInterrupt:
                            break
                        except Exception:
                            raise
            except auth.PermissionDenied:
                print('You are not allowed to manage permissions!')
                break
            except auth.DoesNotExist:
                print('Permission does not exist!')
            except auth.AlreadyExists:
                print('Permission already exists!')

    def delete_user(self, username):
        try:
            while True:
                if self.authorizer.verify_permission('add and delete users', username):
                    print('Enter the name of the user to delete: ')
                    self.authenticator.list_users()
                    user_to_delete = input()
                    self.authenticator.del_user(user_to_delete)
        except auth.PermissionDenied:
            print('You do not have the permission to add and delete users!')
        except auth.DoesNotExist:
            print('The user does not exist!')
