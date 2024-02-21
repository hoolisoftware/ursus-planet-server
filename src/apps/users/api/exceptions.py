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


class ReferrerUsernameNotProvided(APIException):
    status_code = 400
    default_detail = 'Referrer username not provided'
    default_code = 'referrer_username_not_provided'


class ReferrerUsernameInvalid(APIException):
    status_code = 400
    default_detail = 'Given referrer username is invalid'
    default_code = 'referrer_username_invalid'


class ReferrerInvalid(APIException):
    status_code = 400
    default_detail = 'Given referrer invalid'
    default_code = 'referrer_invalid'


class ReferrerAlreadySet(APIException):
    status_code = 400
    default_detail = 'Referrer already set'
    default_code = 'referrer_already_set'


class ReferrerQuoteExceeded(APIException):
    status_code = 400
    default_detail = 'Referrer quote exceeded'
    default_code = 'referrer_quote_exceed'
