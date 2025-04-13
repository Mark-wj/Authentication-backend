from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass  # default fields: username, password, etc.