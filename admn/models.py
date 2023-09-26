from django.db import models
import datetime
# from django.utils.timezone import timezone
# Create your models here.
class registers(models.Model): # contain admins
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=10)
    is_admin=models.BooleanField(default=False)
    def __str__(self):
        return self.name

# choics=('TRUE','true'),('FALSE','false')
days=('saturday','saturday'),('sunday','sunday'),('monday','monday'),('tuesday','tuesday'),('wednesday','wednesday'),('thursday','thursday')
class books(models.Model):
    book_id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=50)
    is_borrowed=models.BooleanField(default=False)
    borrowd_by=models.ForeignKey(registers,on_delete=models.CASCADE,null=True)
    borow_dt=models.TextField(null=True)
    retrn_dt=models.CharField(choices=days,null=True)




# class (models.Model):
#     std_name=models.ForeignKey(registers,on_delete=models.CASCADE,null=True)
#     book_name =models.ForeignKey(books,on_delete=models.CASCADE)



