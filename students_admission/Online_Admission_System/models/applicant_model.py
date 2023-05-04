from django.db import models
from django.db.models import Model
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class ApplicantProfile(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_applications')
    TITTLE_TYPE_CHOICES = [
        ('Mr.','Mr.'),
        ('Mrs.','Mrs.'),
        ('Ms.','Ms.'),
    ]
    Tittle = models.CharField(max_lenghth=10, Choices=TITTLE_TYPE_CHOICES)
    First_Name = models.CharField(max_lenghth=50)
    Middle_Name = models.CharField(max_lenghth=50)
    Last_Name = models.CharField(max_lenghth=50)
    GENDER_TYPE_CHOICES =[
        ('Male','Male'),
        ('Female','Female'),
    ]
    Gender = models.CharField(max_lenghth=10, Choices=GENDER_TYPE_CHOICES)
    DOB = models.DateField()
    Contact = models.IntegerField()
    Email_address = models.CharField(max_lenghth=50, null=True)
    Current_address = models.TextField()
    Permanent_address = models.TextField()
    Fathers_Name = models.CharField(max_lenghth=100)
    Fathers_occupation = models.CharField(max_lenghth=50)
    Mothers_Name = models.CharField(max_lenghth=100)
    Mothers_occupation = models.CharField(max_lenghth=50)
    Nationality = models.CharField(max_lenghth=30)
    Course= models.CharField(max_lenghth=50)
    Academic_Documents = models.FileField(upload_to="documents")
    Student_pic = models.ImageField(upload_to="images")


    def __string__(self):
    return self.First_Name


class ApplicantPrevEducation(models.Model):
    Applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    Highest_level_of_Education = models.CharField(max_lenghth=50)
    Institution_name = models.CharField(max_lenghth=50)
    Year_of_completion = models.DateField()
    Results = models.FileField(upload_to="documents")


    def __string__(self):
        return self.Applicant.First_Name



@receiver(post_save, sender=ApplicantProfile)
def create_profile(sender, instance, created, **kwargs):
    print('signal', '-----', sender)