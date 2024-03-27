from rest_framework.exceptions import APIException


class MissinTaskName(APIException):
    status_code = 400
    default_detail = 'Missing task_name'
    default_code = 'missing_task_name'


class InvalidTaskName(APIException):
    status_code = 400
    default_detail = 'Invalid task name provided'
    default_code = 'invalid_task_name'


class NotFoundTaskLog(APIException):
    status_code = 404
    default_detail = "User isn't completed given task"
    default_code = 'not_found_task_log'
