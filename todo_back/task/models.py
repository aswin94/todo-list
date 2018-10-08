from django.db import models

# Create your models here.


class Task(models.Model): # Our database model is called Task
    TODO = 0
    DONE = 1

    STATUS_CHOICES = ( # We create a tuple of status choices
        (TODO, 'To do'),
        (DONE, 'Done')
    )

    # The tasks description is limited to 255 characters
    description = models.CharField(max_length=255)
    # The task's status, default status = TODO
    status = models.IntegerField(choices=STATUS_CHOICES, default=TODO)