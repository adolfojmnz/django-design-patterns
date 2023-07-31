from django.db import models
from django.conf import settings
from django.utils.functional import cached_property

from .services import SuperHeroWebAPI


class BaseProfile(models.Model):
	USER_TYPES = (
		(0, 'Ordinary'),
		(1, 'SuperHero'),
	)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,
								primary_key=True)
	user_type = models.IntegerField(max_length=1,
									null=True,
									choices=USER_TYPES)
	bio = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		return f"{self.user}: {self.bio or '':.20}"


class SuperHeroProfile(models.Model):
	origin = models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		abstract = True


class OrdinaryProfile(models.Model):
	address = models.CharField(max_length=256, blank=True, null)

	class Meta:
		abstract = True


class Profile(SuperHeroProfile, OrdinaryProfile, BaseProfile):
	pass

