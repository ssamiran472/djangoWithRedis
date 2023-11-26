from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from djangoredis.caches import redis_instance

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


@receiver(post_save, sender=Musician)
def clear_cache_on_create(sender, instance, created, **kwargs):
    if created:
        # Clear or update relevant cache keys
        redis_instance.delete("name")