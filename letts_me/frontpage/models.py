from django.db import models

from hashlib import md5
from datetime import datetime

class Category(models.Model):


    name = models.CharField(max_length = 20)
    parent = models.ForeignKey("Category", blank = True, null = True)
    
    def __str__(self):
        return ((str(self.parent) + ".") if self.parent else "#")  +self.name
    class Meta:
        verbose_name_plural = "categories"

class HasCategory(models.Model):

    categories = models.ManyToManyField(Category, blank = True, null = True)

    class Meta:
        abstract = True


class Gallery(models.Model):

    title = models.CharField(max_length = 50)
    publish_date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "galleries"

class HasGallery(models.Model):

    gallery = models.ForeignKey(Gallery, blank = True, null = True)

    class Meta:
        abstract = True

def upload_path(instance, filename):

    """ 
    upload_path(object, string) -> string
    Generates filepath & filename for new images
    """

    extension = filename.split(".")[-1]
    hsh = md5()
    hsh.update(str(instance))
    new_filename = hsh.hexdigest()
    curr_dt = datetime.now()
    return '/'.join(["gallery",curr_dt.strftime("%y"), curr_dt.strftime("%m"), new_filename + "." + extension])

class Image(models.Model):
    

    img_file = models.ImageField(upload_to = upload_path )
    title = models.CharField(blank = True, max_length = 30)
    description = models.CharField(blank = True, max_length = 140)
    gallery = models.ForeignKey(Gallery)

    
