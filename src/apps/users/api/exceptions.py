from rest_framework.exceptions import APIException


class EmailNotProvidedException(APIException):
    status_code = 400
    default_detail = 'Please provide email'
    default_code = 'email_not_provided'

class EmailAlreadyTaken(APIException):
    status_code = 400
    default_detail = 'Email already taken'
    default_code = 'email_already_taken'


class CodeNotProvided(APIException):
    status_code = 400
    default_detail = 'Code not provided'
    default_code = 'code_not_provided'

class BadCodeProvided(APIException):
    status_code = 400
    default_detail = 'Bad code provided'
    default_code = 'bad_code_provided'