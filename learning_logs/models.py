from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """The topic which the user is studying."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(choices=((False, "Private"),(True, "Public")))

    def __str__(self):
        """Return the string representation model."""
        if len(self.text) <= 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."


class Entry(models.Model):
    """The information studied by the user on the topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return the string representation model"""
        if len(self.text) <= 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
