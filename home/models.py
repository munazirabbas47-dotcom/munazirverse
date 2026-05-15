from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.

phone_validator = RegexValidator(
    regex=r'^\d{11,13}$',
    message="Phone number must contain only numbers and be between 11 to 13 digits."
)

# create model for contact
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,validators=[phone_validator])
    desc = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  'Message From ' + self.name + ' - ' + self.email