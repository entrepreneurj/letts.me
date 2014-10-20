from django.db import models

from fontawesome.fields import IconField

from frontpage.models import HasCategory
    

class Project(HasCategory):

    name = models.CharField(max_length=50)
    repo_url = models.URLField(unique = True)
    repo_icon = IconField()
    description = models.TextField(blank = True)
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

