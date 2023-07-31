from django.db import models

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
    pass


class Comment(Postable):
    pass

