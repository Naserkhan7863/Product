from django.db import models
# Create your models here.
class UserRegisterModel(models.Model):


     user_id=models.AutoField(primary_key=True)
     email=models.EmailField(max_length=100,help_text="Enter Email id")
     contact=models.BigIntegerField(help_text="Enter Mobile Number")
     password=models.CharField(max_length=100,help_text="Enter Password")


     def __str__(self):
         return self.email
         
     
     class Meta:
         db_table="user_details"
    

    
