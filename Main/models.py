from django.db import models

# Create your models here.
# ye class sabhi logo ka data store kregi
class Data(models.Model):
    img=models.FileField(null=True,upload_to='static/imgs/',default='static/imgs/1.jpeg')
    name=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    desc=models.TextField(null=True)
    tdate=models.DateField(null=True)
    fb=models.TextField(null=True)
    google=models.TextField(null=True)
    insta=models.TextField(null=True)
    youtube=models.TextField(null=True)

    def __str__(self):
        return self.name

# ye class sabhi video ko store kregi
class Video(models.Model):
    url=models.CharField(max_length=255,null=True)
    code=models.IntegerField()
    title=models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return self.title,self.code
