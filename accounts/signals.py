from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('Profile created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
            print('Profile did not exist. Created new profile')
#post_save.connect(post_save_create_profile_receiver, sender=User)

def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this is about to be saved')


'''
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

# ✅ Create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('Profile created')
    else:
        # ✅ Ensure profile exists without creating duplicate entries
        instance.userprofile.save()
        print('Profile updated')


# ✅ Print username before saving the UserProfile
@receiver(pre_save, sender=UserProfile)
def pre_save_profile_receiver(sender, instance, **kwargs):
    if instance.user:
        print(instance.user.username, 'this is about to be saved')
'''
'''
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('Profile created')
    else:
        try:
            # Check if profile exists instead of creating it
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
            print('Profile did not exist. Created new profile')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this is about to be saved')
'''