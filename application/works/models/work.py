from django.db import models

from gallery.models.sections import GallerySection


class AbstractContent(models.Model):
    """An instance to define and contain information about the work exposed,
    which can have different GallerySection's it belongs to.
    """
    class Meta:
        abstract = True
        app_label = 'works'

    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    creation_date = models.DateField(null=True)
    uploaded_at = models.DateTimeField(null=True)

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    @property
    def pusblished(self):
        """Verifies whether a work has been published in the site or not. The
        main purpose of this property is to expose only published works in the
        galleries.

        Returns:
            - A Boolean value
        """
        raise NotImplementedError


class BasePortfolioWork(AbstractContent):
    """Some common implementation for all PortfolioWork types of object.
    """
    sections = models.ManyToManyField(GallerySection, null=True)
