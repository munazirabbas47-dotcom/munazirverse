from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.

phone_validator = RegexValidator(
    regex=r"^\d{11,13}$",
    message="Phone number must contain only numbers and be between 11 to 13 digits.",
)


# create model for contact
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    
    name = models.CharField(
        max_length=255,
        validators=[
            MinLengthValidator(3, message="Name must be at least 3 characters long.")
        ],
    )

    email = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(4, message="Email must be at least 4 characters long.")
        ],
    )

    phone = models.CharField(max_length=13, validators=[phone_validator])

    desc = models.TextField(
        validators=[
            MinLengthValidator(
                4, message="Description must be at least 4 characters long."
            )
        ]
    )

    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Message From " + self.name + " - " + self.email
