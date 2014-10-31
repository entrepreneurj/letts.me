from django.db import models

from hashlib import md5
from datetime import datetime

from django.db.models.signals import pre_save
from django.dispatch import receiver

class Category(models.Model):


    name = models.CharField(max_length = 20)
    parent = models.ForeignKey("Category", blank = True, null = True)
    ancestor = models.ForeignKey("Category", blank = True, null = True, related_name="descendent")

    def __str__(self):
        return ((str(self.parent) + ".") if self.parent else "#")  +self.name
    
    def get_root(self):
        # returns the root category, even if self
        return self.parent.get_root() if self.parent else self

    class Meta:
        verbose_name_plural = "categories"

@receiver(pre_save, sender=Category)
def category_pre_save(sender, **kwargs):

    # Update's cateegory ancestor with each save
    instance = kwargs["instance"]
    instance.ancestor = instance.get_root()


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

    
