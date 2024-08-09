from django.db import models
from django.contrib.auth.models import User

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.CharField(max_length=64, unique=True)
    created_when = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"

class Task(models.Model):
	title = models.CharField(max_length=200)
	# complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title