import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def thread_checking_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")


print(f"Main code thread ID: {threading.get_ident()}")  #check threadID and created user
user = User.objects.create(username='mainuser')