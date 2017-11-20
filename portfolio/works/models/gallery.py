from django.db import models


# class Gallery(models.Model):
#     gallery_theme = models.CharField(null=True)
#
#     class Meta:
#         verbose_name = 'gallery'
#         verbose_name_plural = 'galleries'
#
#     def __str__(self):
#         return 'Gallery'


class GallerySection(models.Model):
    # gallery = models.ForeignKey(Gallery, related_name='sections', null=True, on_delete=True)
    title = models.CharField(max_length=120, null=True)

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
        return '<%s %s: %s %s>' % (self.title,
                                   self.__class__.__name__,
                                   'name',
                                   'test')
