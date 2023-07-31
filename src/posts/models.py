from django.db import models
from django.conf import settings

from .managers import PostManager


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now =True)

    class Meta:
        abstract = True


class Postable(TimeStampedModel):
    message = models.TextField(max_length=500)

    class Meta:
        abstract = True


class Post(Postable):
    POST_PRIVACY = (
        ('public', 'Public'),
        ('individual', 'Individual')
    )
    privacy = models.CharField(max_length=12, choices=POST_PRIVACY,
                               default='public')
    # A recipient is needed if the privacy is set to "Individual"
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  blank=True,
                                  null=True,
                                  related_name="recieved_posts")
    objects = PostManager()


class Comment(Postable):
    pass

