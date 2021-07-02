from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=False, blank=False)
    salary = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'name'
        verbose_name_plural = 'names'
