from django.db import models

from .gallery import Gallery


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
