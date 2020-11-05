# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class City(models.model):
    name = models.charfield(max_length=25)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural = 'cities'
