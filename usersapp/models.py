from django.db import models
import datetime

# Create your models here.
class UserModels(models.Model):
    user_id = models.AutoField(primary_key=True)
    date = models.DateField(default=datetime.date.today)
    name = models.TextField(max_length=50, null=True)
    # username = models.TextField(max_length=25, null=True)
    contact = models.TextField(max_length=25, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.TextField( max_length=8, null=True)   
    file = models.FileField( upload_to='images', null=True)
    user_status=models.TextField(max_length=30,default='pending',null=True)
    Otp_Status = models.TextField(max_length=20, default='pending')
    otp = models.IntegerField(null=True)
    
    class  Meta:
        db_table = 'user_details'

class Predict_details(models.Model):
    predict_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length = 60, null = True)
    age = models.CharField(max_length = 60, null = True)
    hypertension = models.TextField(max_length = 60, null = True)
    heart = models.CharField(max_length = 60, null = True)
    married = models.CharField(max_length = 60, null = True)
    work = models.CharField(max_length = 60, null = True)
    residence = models.CharField(max_length = 60, null = True)
    bmi = models.TextField(max_length = 60, null = True)
    glucose = models.TextField(max_length = 60, null = True)
    # cholestrol = models.TextField(max_length = 60, null = True)
    # bp_h = models.TextField(max_length = 60, null = True)
    # bp_l = models.TextField(max_length = 60, null = True)
    # alochol = models.TextField(max_length = 60, null = True)
    smoking = models.TextField(max_length = 60, null = True)

    class Meta:
        db_table = "predict_detail"