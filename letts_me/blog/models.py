from django.db import models


# Blog Entry
class Entry(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    draft = models.BooleanField(default = True)
    published = models.DateTimeField(auto_now_add = True)
    def summary(self):
        return "{0}...".format(' '.join(self.text.split()[:50]))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published']
