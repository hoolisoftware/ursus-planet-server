from rest_framework.exceptions import APIException


class AlreadyGotRewardException(APIException):
    status_code = 400
    default_detail = "User already got given task reward"
    default_code = 'already_got_task_reward'
