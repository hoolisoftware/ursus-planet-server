from dataclasses import dataclass


@dataclass
class Task:
    name: str
    title: str
    app: str
    cancellable = False


class TaskUsername(Task):
    name = 'task_username'
    title = 'Task - set username'
    app = 'users'


class TaskEmail(Task):
    name = 'task_email'
    title = 'Task - set email'
    app = 'users'


class TaskAvatar(Task):
    name = 'task_avatar'
    title = 'Task - set avatar'
    app = 'users'


class TaskReferrer(Task):
    name = 'task_referrer'
    title = 'Task - set referrer'
    app = 'users'


class TaskCabinetNotificationsAccount(Task):
    name = 'task_cabinet_notifications_account'
    title = 'Task - enable cabinet account notifications'
    app = 'users'


class TaskCabinetNotificationsEmail(Task):
    name = 'task_cabinet_notifications_email'
    title = 'Task - enable cabinet email notifications'
    app = 'users'


class TaskSocialDiscord(Task):
    name = 'task_social_discord'
    title = 'Task - connect Discord account'
    cancellable = True
    app = 'socials'


class TaskSocialGithub(Task):
    name = 'task_social_github'
    title = 'Task - connect Github account'
    cancellable = True
    app = 'socials'


class TaskSocialTelegram(Task):
    name = 'task_social_telegram'
    title = 'Task - connect Telegram account'
    cancellable = True
    app = 'socials'


class TaskSocialX(Task):
    name = 'task_social_x'
    title = 'Task - connect X account'
    cancellable = True
    app = 'socials'
