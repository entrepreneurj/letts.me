from django.db import models

from frontpage.models import HasCategory

class EntryManager(models.Manager):

    use_for_related_fields = True

    def get_queryset(self):
        return super(EntryManager, self).get_queryset().filter(draft = False)
    
    def latest(self, **kwargs):
        return self.get_queryset()[0]

# Blog Entry
class Entry(HasCategory):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    draft = models.BooleanField(default = True)
    publish_date = models.DateTimeField(auto_now_add = True)

    objects = models.Manager()
    published = EntryManager()

    def summary(self):
        return "{0}...".format(' '.join(self.text.split()[:50]))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"
        ordering = ['-publish_date']
