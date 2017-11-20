from django.db import models

from .gallery import GallerySection


class AbstractPortfolioWork(models.Model):
    """An instance to define and contain information about the work exposed, which can have
    different GallerySection's it belongs to.
    """

    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    creation_date = models.DateField(null=True)
    uploaded_at = models.DateTimeField(null=True)

    sections = models.ManyToManyField(GallerySection)
