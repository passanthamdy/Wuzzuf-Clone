from email import charset
from django.db import models
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator
# Create your models here.
GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'Female'),
    
)
LEVELS = (
    ('JUNIOR', 'Junior'),
    ('SENIOR', 'Senior'),
    ('ENTRY_LEVEL',"Entry level")
    
)
SIZE=(
    ('LESS_50','Less than 50'),
    ('50_200','From 50 to 200'),
    ('200_500', 'From 200 to 500'),
    ('MORE_500', 'More than 500')
)


class City(models.Model):
    name=models.CharField( max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user=models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    first_name=models.CharField( max_length=50)
    last_name =models.CharField( max_length=50)
    gender = models.CharField(choices=GENDER, max_length=50)
    dob = models.DateField(default=now)
    cv = models.FileField(upload_to='user_cvs/', null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    level=models.CharField(choices=LEVELS, max_length=50, default="ENTRY_LEVEL")
    job_title=models.CharField(max_length=50)
    city=models.ForeignKey("profiles.City", blank=True,null=True, on_delete=models.SET_NULL)
    city_alert= models.BooleanField(default=False)

    def __str__(self):
        return self.first_name +" "+self.last_name


class Company(models.Model):
    user=models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    about=models.TextField(blank=True, null=True)
    industry=models.CharField(max_length=50)
    company_size=models.CharField(choices=SIZE, max_length=50, default="LESS_50")
    started_at=models.DateField()
    website= models.URLField(max_length = 200, blank=True, null=True)
    city=models.ForeignKey("profiles.City", blank=True,null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.company_name
    


    