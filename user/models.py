from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Avg
from accounts import models as accountmodels



# Create your models here.

class Specialties(models.Model):
    name=models.CharField(verbose_name='التخصص' , max_length=50 , null=True , blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    genders=(
        ('Male','Male'),
        ('female','female'),
    )
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    name=models.CharField(verbose_name='الاسم' , max_length=50 , null=True , blank=True)
    Specialist_doctor=models.ForeignKey(Specialties, on_delete=models.PROTECT , null=True , blank=True)
    address=models.CharField(verbose_name='العنوان' , max_length=50 , null=True , blank=True)
    Waiting_time=models.CharField(verbose_name='مدة الانتظار' , max_length=50 , null=True , blank=True)
    working_hours=models.CharField(verbose_name='عدد ساعات العمل' , max_length=50 , null=True , blank=True)
    phone_number=models.CharField(verbose_name='رقم الهاتف' , max_length=50 , null=True , blank=True)  
    who_i=models.TextField(verbose_name='من انا',max_length=100 , null=True , blank=True)
    price = models.IntegerField(verbose_name='سعر الكشف',null=True , blank=True)
    facebook=models.CharField(max_length=50 , null=True , blank=True)
    twitter=models.CharField( max_length=50 , null=True , blank=True)
    gmail=models.CharField( max_length=50 , null=True , blank=True)
    gender=models.CharField(max_length=50 ,null=True , blank=True ,choices=genders )
    image=models.ImageField(upload_to='profile_image' , null=True , blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    favourite=models.ManyToManyField(User , related_name='favourites',blank=True)
    slug=models.SlugField(max_length=50 , null=True , blank=True)
    
    @property
    def get_rate(self):
        rates=accountmodels.Rate.objects.filter(doctor=self.user).aggregate(average=Avg('rate'))
        average=rates['average']
        if average is None:
            return 0
        else:
            return round(average)
    @property
    def get_comments_count(self):
        total=accountmodels.Comment.objects.filter(doctor=self.user).count()
        return total

    def save(self, *args, **kwargs):
        self.slug=slugify(self.user.username)
        super(Doctor,self).save(*args , **kwargs)

    
    def __str__(self):
        return str(self.user)
