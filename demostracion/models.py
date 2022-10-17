from django.db import models


class Person(models.Model):
    id = models.BigAutoField
    nombre = models.CharField(max_length=200)

    def idd(self):
        return self.id

    def nombree(self):
        return self.nombre
