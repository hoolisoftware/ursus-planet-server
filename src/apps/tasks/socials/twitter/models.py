from django.db import models

from apps.tasks.models import Task, ProjectField


class ProfileMixin(models.Model):
    link_prorile = models.URLField()

    class Meta:
        abstract = True


class TweetMixin(models.Model):
    link_tweet = models.URLField()

    class Meta:
        abstract = True


class ProfileFollowTask(ProfileMixin, Task):
    project = ProjectField('twitter_profile_follow')


class TweetRepostTask(TweetMixin, Task):
    project = ProjectField('twitter_tweet_repost')


class TweetLikeTask(TweetMixin, Task):
    project = ProjectField('twitter_tweet_like')


class TweetCommentExactTask(TweetMixin, Task):
    project = ProjectField('twitter_tweet_comment_exact')
    text = models.TextField()


class TweetCommentTask(TweetMixin, Task):
    project = ProjectField('twitter_tweet_comment')


class TweetWatchVideoTask(TweetMixin, Task):
    pass


class TweetTask(Task):
    text = models.TextField()