from rest_framework.exceptions import APIException


class ReferrerUsernameNotProvided(APIException):
    status_code = 400
    default_detail = 'Referrer username not provided'
    default_code = 'referrer_username_not_provided'


class ReferrerUsernameInvalid(APIException):
    status_code = 400
    default_detail = 'Given referrer username is invalid'
    default_code = 'referrer_username_invalid'


class ReferrerInvalid(APIException):
    '''
        raises when given referrer doesn't satisfy conditions
        - have username
        - have referrer
    '''
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
