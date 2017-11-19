from django.db import models


class Gallery(models.Model):
    theme = models.CharField()


class GallerySection(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='sections')
