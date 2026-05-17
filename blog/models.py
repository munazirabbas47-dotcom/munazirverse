from django.db import models

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    heading1 = models.CharField(max_length=100,default="")
    contant1 = models.CharField(max_length=5000,default="")
    heading2 = models.CharField(max_length=50,default="")
    contant2 = models.CharField(max_length=5000,default="")
    heading3 = models.CharField(max_length=100,default="")
    contant3 = models.CharField(max_length=5000,default="")
    publish_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog_image",default="")
    
    def __str__(self):
        return self.title
