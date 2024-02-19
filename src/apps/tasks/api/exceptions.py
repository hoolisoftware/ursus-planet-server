from rest_framework.exceptions import APIException


class InvalidTaskName(APIException):
    status_code = 400
    default_detail = 'Invalid task name provided'
    default_code = 'invalid_task_name'


class NotFoundTaskLog(APIException):
    status_code = 404
    default_detail = "User isn't completed given task"
    default_code = 'not_found_task_log'


class AlreadyGotReward(APIException):
    status_code = 400
    default_detail = "User already got given task reward"
    default_code = 'already_got_task_reward'
