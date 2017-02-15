from django.db import models
import uuid

class user(models.Model):
  #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=30)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=32)
  isadmin = models.BooleanField()
  def __unicode__(self):
    return self.name

class item(models.Model):
  #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=30)
  quantity = models.IntegerField()
  sled = models.DateField()
  def __unicode__(self):
    return self.name
