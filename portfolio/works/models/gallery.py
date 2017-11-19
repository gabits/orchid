from django.db import models


class Gallery(models.Model):
    theme = models.CharField()


class GallerySection(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='sections')
    title = models.CharField(max_length=120)

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
                                                             gallery=self.gallery)

    def __repr__(self):
        return '<%s %s: %s %s>' % (self.title,
                                   self.__class__.__name__,
                                   super().__name___,
                                   self.gallery)
