from django.db import models
from django.contrib.auth.models import User

class Designer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_link = models.URLField()
    bio = models.TextField()

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"

class Portfolio(models.Model):
    designer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
# marketplace/models.py

# marketplace/models.py

from django.db import models
from django.contrib.auth.models import User

class Designer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='designers/')
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()

class Project(models.Model):
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE)
    # Other fields removed and added in migration

# Other models...

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    designer = models.ForeignKey('Designer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
