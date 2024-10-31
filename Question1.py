import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def sync_signal_handler(sender, instance, **kwargs):
    print("Signal received. Starting processing...")
    time.sleep(3)  
    print("Signal processing completed.")


user = User.objects.create(username='mainuser')
print("User creation complete.")
