from django.db import models


# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=200)
    discord_uid=models.AutoField
    def __str__(self):
        return self.name

class guild(models.Model):
    name=models.CharField(max_length=200)
    guild_uid=models.AutoField
    members=models.ManyToManyField(user)
    def __str__(self):
        return self.name

class match(models.Model):
    guild_uid1=models.IntegerField
    guild_uid2=models.IntegerField