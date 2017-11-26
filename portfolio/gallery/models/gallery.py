from django.db import models


class Gallery(models.Model):
    """A Gallery is an instance that contains sections, which will contain works
    to be displayed.
    It has a title that will identify it, i.e. Colors Study Gallery.
    """

    title = models.CharField(max_length=255, null=True)

    css_class = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'
        db_table = 'gallery'
        app_label = 'gallery'

    def __str__(self):
        return 'Gallery'

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__,
                             self.title)
