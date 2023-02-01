from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.username


class Certificate(models.Model):
    grade = models.IntegerField(default=0)
    date_of_creation = models.DateTimeField(default=timezone.now())
    description = models.TextField()
    transaction_id = models.TextField(null=True, blank=True, editable=False)
    student = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Certificate")
        verbose_name_plural = ("Certificates")

    def __str__(self):
        return self.description












