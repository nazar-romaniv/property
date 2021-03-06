import hashlib
from main import Agent

class User(Agent):

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = User.__encrypt(password)
        self.logged_in = False

    @staticmethod
    def __encrypt(password: str):
        password = password.encode('utf-8')
        return hashlib.sha256(password).hexdigest()

    def verify_password(self, to_verify):
        to_verify = to_verify.encode('utf-8')
        to_verify = hashlib.sha256(to_verify).hexdigest()
        return to_verify == self.password


class Authenticator:

    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if len(password) < 6:
            raise PasswordTooShort
        if username in self.users:
            raise AlreadyExists
        self.users[username] = User(username, password)

    def log_in(self, username, password):
        try:
            user = self.users[username]
            if user.logged_in:
                raise AlreadyLoggedIn
            if not user.verify_password(password):
                raise InvalidPassword
            user.logged_in = True
            return True
        except KeyError:
            raise DoesNotExist

    def is_logged_in(self, username):
        try:
            if self.users[username].logged_in:
                return True
            return False
        except KeyError:
            return False

    def del_user(self, username):
        try:
            del self.users[username]
        except KeyError:
            raise DoesNotExist

    def list_users(self):
        for user in self.users:
            print(user)
        print()


authenticator = Authenticator()


class Authorizer:

    def __init__(self):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, perm_name):
        if perm_name in self.permissions:
            raise AlreadyExists
        self.permissions[perm_name] = set()

    def give_permission(self, perm_name, username):
        try:
            user = self.authenticator.users[username]
            permission = self.permissions[perm_name]
        except KeyError:
            raise DoesNotExist
        else:
            permission.add(user)

    def withdraw_permission(self, perm_name, username):
        try:
            user = self.authenticator.users[username]
            permission = self.permissions[perm_name]
            permission.remove(user)
        except KeyError:
            raise DoesNotExist

    def verify_permission(self, perm_name, username):
        try:
            user = self.authenticator.users[username]
            if user in self.permissions[perm_name]:
                return True
            else:
                raise PermissionDenied
        except KeyError:
            raise DoesNotExist

    def list_permissions(self, username):
        try:
            user = self.authenticator.users[username]
        except KeyError:
            raise DoesNotExist
        perm_list = []
        for permission in self.permissions:
            if user in self.permissions[permission]:
                perm_list.append(permission)
        return perm_list

    def print_permissions(self):
        for permission in self.permissions:
            print(permission)


class InvalidPassword(Exception):
    pass


class DoesNotExist(Exception):
    pass


class AlreadyExists(Exception):
    pass


class PasswordTooShort(Exception):
    pass


class AlreadyLoggedIn(Exception):
    pass


class PermissionDenied(Exception):
    pass


authorizer = Authorizer()
authorizer.add_permission('add a new entry')
authorizer.add_permission('delete entries')
authorizer.add_permission('view information about properties')
authorizer.add_permission('add and delete users')
authorizer.add_permission('manage permissions')
