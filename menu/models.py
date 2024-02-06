from django.db import models
from django.db.models import Q


class Menu(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    menu = models.ForeignKey(Menu, blank=True,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               on_delete=models.CASCADE)

    url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.title



