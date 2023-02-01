from django.db import models

class Certificate(models.Model):
    grade = models.IntegerField(default=0)
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=200)
    transaction_id = models.TextField(null=True, blank=True, editable=False)
    student = models.ForeignKey("Student", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Certificate")
        verbose_name_plural = ("Certificates")

    def __str__(self):
        return self.transaction_id


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    cartificate = models.ForeignKey("Certificate", null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.name + ' ' + self.last_name








