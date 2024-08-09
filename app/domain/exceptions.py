class DomainError(Exception): ...


class AuthenticationError(DomainError):
    "Error occurred in athorization process"
    ...


class NoPermissionError(DomainError): 
    "User doent have permission to do this action"
    ...
