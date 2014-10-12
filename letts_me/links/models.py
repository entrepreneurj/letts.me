from django.db import models

from blog.models import Entry


class LinkManager(models.Manager):

    def latest(self):
        return self.get_queryset()[0]

class Link(models.Model):

    title = models.CharField(max_length = 144)
    description = models.CharField(max_length = 200)
    url = models.URLField(unique = True)
    date_submitted = models.DateTimeField(auto_now = True)
    blog_entry = models.ForeignKey(Entry, blank = True, null = True)    
    
    objects = models.Manager()
    link_manager = LinkManager()
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_submitted']



