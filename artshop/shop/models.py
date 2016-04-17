from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class ShopUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return 'ShopUser(id=%s, username=%s, email=%s)' % (self.id, self.username, self.email)


class ShopUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')



