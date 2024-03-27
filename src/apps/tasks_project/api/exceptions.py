from rest_framework.exceptions import APIException


class MissingTaskIdException(APIException):
    status_code = 400
    default_detail = 'Missing task_id'
    default_code = 'missing_task_id'


class InvalidTaskIdException(APIException):
    status_code = 400
    default_detail = 'Invalid task_id'
    default_code = 'invalid_task_id'
