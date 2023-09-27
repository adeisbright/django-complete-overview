from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="Lorem")
    tags = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    venue = models.CharField(max_length=100, default="Lagos")
    event_type = models.CharField(max_length=10)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # This makes the table to list the items in events by showing the title
    def __str__(self) -> str:
        return self.title
