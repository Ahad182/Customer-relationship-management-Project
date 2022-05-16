from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

class User(AbstractUser):
    is_orgnaizer = models.BooleanField(default=False , null=True )
    is_agent = models.BooleanField(default=False , null=True )
    
    
    


class UserProfile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} "


class Lead(models.Model):

    SOURCE_CHOICES = (
        ('Facebook','Facebook'),
        ('Google','Google'),
        ('Youtube','Youtube'),
        ('Twitter','Twitter'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    sources = models.CharField(choices=SOURCE_CHOICES,max_length=255)
    agent = models.ForeignKey ("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey ("UserProfile", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey ("Category", related_name="leads" , null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True)
    discription = models.TextField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    photo = models.ImageField(upload_to='profile_pictures/',null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"




def handle_upload_folloups_file(instance,filename):
    return f"lead_followups/lead_{instance.lead.pk}/{filename}"

class FollowUp(models.Model):
    lead = models.ForeignKey('Lead',related_name='followups', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True,null=True)
    first_name = models.FileField(null=True, blank=True,upload_to=handle_upload_folloups_file)

    def __str__(self):
        return f"{self.lead.first_name} {self.lead.last_name}"




class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    organization = models.ForeignKey ("UserProfile", on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.user.username} "





class Category(models.Model):
    name = models.CharField( max_length=30)
    organization = models.ForeignKey ("UserProfile", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}"





def post_user_created_signal(sender , instance , created , **kwargs):
   if created:
       UserProfile.objects.create(user=instance)



post_save.connect(post_user_created_signal , sender=User)