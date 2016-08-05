from django.db import models

# Create your models here.

class Message(models.Model):
    ms_title = models.CharField(max_length=30)
    ms_content = models.TextField()
    ms_pub_date = models.DateTimeField()

    def __str__(self):
        return self.ms_title


