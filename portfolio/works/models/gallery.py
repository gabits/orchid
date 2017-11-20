from django.db import models


class Gallery(models.Model):
    """A Gallery is an instance that contains sections, which will contain works
    to be displayed.
    It has a title that will identify it, i.e. Colors Study Gallery.
    """

    title = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'galleries'
        db_table = 'gallery'

    def __str__(self):
        return 'Gallery'

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__,
                             self.title)


class GallerySection(models.Model):
    """Section of a specific gallery, containing a theme and an optional
    description, and it's linked to PortfolioWork's it'll display.
    """

    gallery = models.ForeignKey(Gallery, related_name='sections', null=True)
    theme = models.CharField(max_length=120, null=True)

    class Meta:
        verbose_name = 'gallery_section'
        verbose_name_plural = 'gallery_sections'
        db_table = 'gallery_sections'

        permissions = (
            ('create_section', 'Can create a new section in the gallery'),
            ('view_section', 'Can view section in the gallery'),
        )

    def __str__(self):
        return '{title} section in gallery {gallery}'.format(title=self.title,
                                                             gallery='test')

    def __repr__(self):
        return '<%s %s: %s %s>' % (self.theme,
                                   self.__class__.__name__,
                                   'name',
                                   'test')
