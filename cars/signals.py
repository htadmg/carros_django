from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cars.models import Car

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('------post delete------')
    print(instance)
