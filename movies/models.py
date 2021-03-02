from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre name",
help_text='Enter a film genre (e.g. sci-fi, comedy)')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name