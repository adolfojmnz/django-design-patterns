from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.functional import cached_property

from .services import SuperHeroWebAPI


class BaseProfile(models.Model):
	USER_TYPES = (
		(0, 'Ordinary'),
		(1, 'SuperHero'),
	)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,
			     				on_delete=models.CASCADE,
								primary_key=True)
	user_type = models.IntegerField(choices=USER_TYPES, null=True)
	bio = models.CharField(max_length=256, blank=True, null=True)

	def is_superhero(self):
		return SuperHeroWebAPI.is_hero(self.user.username)

	@cached_property
	def age(self):
		today = timezone.datetime.today()
		return (today.year - self.birthdate.year) - int(
			(today.month, today.day) <
			(self.birthdate.moth, self.birthdate.day))

	@cached_property
	def full_name(self):
		return f"{self.firstname}, {self.lastname}"

	def __str__(self):
		return f"{self.user}: {self.bio or '':.20}"


class SuperHeroProfile(models.Model):
	origin = models.CharField(max_length=128, blank=True, null=True)

	class Meta:
		abstract = True


class OrdinaryProfile(models.Model):
	address = models.CharField(max_length=256, blank=True, null=True)

	class Meta:
		abstract = True


class Profile(SuperHeroProfile, OrdinaryProfile, BaseProfile):
	pass

