from django.db import models

# Create your models here.

class Department(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_description=models.CharField(max_length=150)

    def __str__(self):
        return self.dep_name
    
class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.stu_name
    

    