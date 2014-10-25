from django.db import models
from django.template.defaultfilters import slugify

from fontawesome.fields import IconField

from frontpage.models import HasCategory
    

class Project(HasCategory):

    name = models.CharField(max_length=50)
    slug = models.SlugField(null = True)
    repo_url = models.URLField(blank = True, null=True)
    repo_icon = IconField()
    demo_url = models.URLField( blank = True, null=True)
    description = models.CharField(blank = True, max_length = 70)
    summary = models.TextField(blank=True, null = True)
    completion = models.IntegerField(default = 0)
    HI = '1'
    MED = '2'
    LO = '3'
    IMPORTANCE_CHOICES = (
        (HI, 'Most Important'),
        (MED, 'Average Importance'),
        (LO, 'Least Important')
    )
    importance = models.CharField(max_length = 1, choices = IMPORTANCE_CHOICES, 
                                    default = MED)

    def __str__(self):
        return "Project: " + self.name

    class Meta:
        ordering = ['importance']
