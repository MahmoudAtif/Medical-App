from user.models import *
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save ,sender =User)
def create_profile(sender , instance , created , **kwargs):
    if created:
        Doctor.objects.create(
            user=instance,
            name=instance.username,
            slug=instance.username,
        )

# post_save.connect(create_profile , sender=User)


# @receiver(post_save ,sender =Appointment)
# def create_appointment(sender , instance , created , *args , **kwargs):
#     if created:
#         Appointment.objects.create(
#             user=instance,
#             gmail=instance.user.profile.gmail,
#             phone_number=instance.user.profile.phone_number
#         )