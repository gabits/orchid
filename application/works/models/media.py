from django.db import models
from .work import AbstractContent


class BaseImageContent(AbstractContent):
    """Contains an url to a visual piece of work it refers to.
    """

    # TODO: instead of an url, store images using a Django field.
    image_url = models.CharField(max_length=255)


class BaseAudiovisualContent(AbstractContent):
    """Contains an url to an audiovisual piece of work it refers to.
    """
    # TODO: implement video stream and audio reproduction instead of pointing to an URL.
    audiovisual_url = models.CharField(max_length=255)


class Photograph(BaseImageContent):

    class Meta:
        verbose_name = 'photograph'
        verbose_name_plural = 'photographs'
        db_table = 'photograph'


class Video(BaseAudiovisualContent):

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        db_table = 'video'
