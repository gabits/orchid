from django.db import models


class AbstractPortfolioWork(models.Model):
    """An instance to define and contain information about the work exposed, which can have
    different categories.
    """
    title = models.CharField(max_lenght=255)
    description = models.TextField()

    creation_date = models.DateField()
    uploaded_at = models.DateTimeField()

