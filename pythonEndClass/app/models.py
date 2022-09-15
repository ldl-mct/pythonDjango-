from django.db import models
class enteriModel(models.Model):
    id = models.AutoField(primary_key=True)
    xingming = models.CharField(max_length=8)
    xuehao = models.CharField(max_length=4,unique=True)
    dianhua = models.CharField(max_length=11)
    mima = models.CharField(max_length=12)
    gender = models.CharField(max_length=4)
    jianjie = models.CharField(max_length=100)
    src = models.FileField(upload_to="images")
    class Meta:
        db_table = "enteritable"

