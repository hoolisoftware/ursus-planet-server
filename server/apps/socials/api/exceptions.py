from rest_framework.exceptions import APIException


class AccountAlreadyTaken(APIException):
    status_code = 403
    default_detail = 'This social account is already associated with another user.'
    default_code = 'account_already_taken'


class AccountNotFound(APIException):
    status_code = 404
    default_detail = 'Social account not found'
    default_code = 'not_found'


class SomethingWentWrong(APIException):
    status_code = 400
    default_detail = 'Something went wrong, try again.'
    default_code = 'something_went_wrong'


class SocialNotProvided(APIException):
    status_code = 400
    default_detail = 'Please provide the social'
    default_code = 'social_not_provided'


class SocialNotSupported(APIException):
    status_code = 400
    default_detail = 'Usupported social provided'
    default_code = 'unsupported_social'


class CodeNotProvided(APIException):
    status_code = 401
    default_detail = 'Please provide the code'
    default_code = 'code_not_provided'


class BadCodeProvided(APIException):
    status_code = 401
    default_detail = 'Bad code provided'
    default_code = 'bad_code_provided'