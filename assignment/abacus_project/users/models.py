from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=[
            ('owner', 'Owner'),
            ('employee', 'Employee')
        ]
    )

    def __str__(self):
        return self.username
