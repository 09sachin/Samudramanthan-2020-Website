from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField

OPTIONS = (
("event a","event a"),
    ("Offshore Riggers", "Offshore Riggers"),
    ("Naval warfare", "Naval warfare"),
    ("Data tussle", "Data tussle"),
    ("Case Study","Case Study"),
("Beyond 2","Beyond 2"),
("OCEANIA QUIZ","OCEANIA QUIZ"),
("PAPER PRESENTATION","PAPER PRESENTATION"),
("Blockchain Workshop","Blockchain Workshop"),
)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(
    #     upload_to = 'assets/images',
    #     default = 'no-img.jpg',
    #     blank=True
    # )
    first_name = models.CharField(max_length=255, default='')
    events = MultiSelectField(max_length=300, choices=OPTIONS)
    email = models.EmailField(default='none@email.com')
    birth_date = models.DateField(default='1999-12-31')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    College = models.CharField(max_length=255, default='')
    Contact = models.CharField(max_length=255, default='')
    # events = MultiSelectField(max_length=300, choices=OPTIONS)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

