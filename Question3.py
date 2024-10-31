from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def transaction_test_handler(sender, instance, **kwargs):
    instance.first_name = "Signal Changed"
    instance.save() 
    print("Signal handler executed and user first_name updated.")

try:
    with transaction.atomic():
        user = User.objects.create(username='testuser')
        raise Exception("Simulating an error after user creation")
except Exception as e:
    print("Exception occurred, transaction should be rolled back.")


print("User exists:", User.objects.filter(username='mainuser').exists())