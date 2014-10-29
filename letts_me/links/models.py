from django.db import models

from blog.models import Entry

from frontpage.models import HasCategory

class LinkManager(models.Manager):
    
    use_for_related_fields = True

    def latest(self):
        return self.get_queryset()[0]

    def get_queryset(self):
        return super(LinkManager, self).get_queryset().filter(draft = False)

class Link(HasCategory):

    title = models.CharField(max_length = 144)
    description = models.CharField(max_length = 200)
    url = models.URLField(unique = True)
    date_submitted = models.DateTimeField(auto_now_add = True)
    blog_entry = models.ForeignKey(Entry, blank = True, null = True)    
    draft = models.BooleanField(default = False)
    objects = models.Manager()
    link_manager = LinkManager()
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_submitted']



