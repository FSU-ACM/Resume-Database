from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
	is_student = models.BooleanField(defualt=False)
	is_companyrep = models.BoolenaField(default=False)
#	is_admin = models.BooleanField(default=False)

class Student(models.Model):
	user = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
	resume = models.ManyToManyField(Resume, through='ResumeSubmitted')
	cover_letter = models.ManyToManyField(Cover_Letter, through='CoverLetterSumbitted)

