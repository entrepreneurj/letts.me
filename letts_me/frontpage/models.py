from django.db import models


class Category(models.Model):


    name = models.CharField(max_length = 20)
    parent = models.ForeignKey("Category", blank = True, null = True)
    
    def __str__(self):
        return "#"+ ( (self.parent.name + ".") if self.parent else "")  +self.name
    class Meta:
        verbose_name_plural = "categories"

class HasCategory(models.Model):

    categories = models.ManyToManyField(Category, blank = True, null = True)


    class Meta:
        abstract = True
