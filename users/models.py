from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

import re,datetime
def validate_mobile(mobile):
    regex = "[6-9]\d{9}"
    if not re.fullmatch(regex,mobile):
        raise ValidationError("Invalid mobile number")




class Person(models.Model):
    id = models.CharField(max_length=30,primary_key=True,editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256,unique=True)
    mobile = models.CharField(max_length=10,unique=True,validators=[validate_mobile])
    slug = models.SlugField(editable=False,null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.full_name)
        if not self.id:
            self.id = datetime.datetime.now().strftime("%d%m%Y%H%M%S%f")
        super(Person,self).save(*args,**kwargs)

    def __str__(self):
        return self.full_name