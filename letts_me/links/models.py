from django.db import models


class Link(models.Model):

    title = models.CharField(max_length = 144)
    description = models.CharField(max_length = 200)
    url = models.URLField(unique = True)
    date_submitted = models.DateTimeField(auto_now = True)
    

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_submitted']
