from django.db import models
import random
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from models.applicant_model import ApplicantProfile


class Application(models.Model):  
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='owner_applications')
    applicant = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE, related_name='applicant_applications')
    subject = models.ForeignKey(InstitutionSubject, on_delete=models.CASCADE, related_name='subject_applications')
    STATUS_CHOICES = [
        ('0', 'rejected'),
        ('1', 'Completed'),
        ('2', 'Canceled'),
        ('3', 'Pending')
    ]
    status = models.CharField(max_length=10, Choices=STATUS_CHOICES, default='3')
    LEVEL_CHOICES = [
        ('0', 'Certificate'),
        ('1', 'Diploma'),
        ('2', 'Bachelor'),
        ('3', 'Masters'),
        ('4', 'Phd'),
    ]
    level = models.CharField( max_length=10, Choices=LEVEL_CHOICES)
    paid = models.BooleanField(default=False)
    admit_card = models.FileField(upload_to="admit_card", null=True, blank=True)
    created_at = models.DateTimeField( auto_now=True)
