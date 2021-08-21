from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("email field is required")
        
        email = self.normalize_email(email)
        user =  self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# create Custom user model to authenticate with email and password instead of default username and apssword
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email



# create profile model to store Basic information about user.
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField(max_length=264,blank=True)
    last_name = models.CharField(max_length=264,blank=True)
    address = models.TextField(max_length=350, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    Country = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',verbose_name='Profile Photo')
    dob = models.DateField(blank=True, verbose_name='Date of Birth',null=True)
    facebook_id = models.URLField(blank=True, verbose_name='Facebok Id')


    def __str__(self):
        return self.first_name + " " + self.last_name


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
