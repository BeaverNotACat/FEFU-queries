class DomainError(Exception): ...


class AuthenticationError(DomainError):
    "Error occurred in athorization process"

    ...


class UserDoesNotExist(AuthenticationError):
    "You have tired to login as user that does not exist"

    ...


class NoPermissionError(DomainError):
    "User doent have permission to do this action"

    ...
