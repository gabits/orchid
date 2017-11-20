from django.db import models
from .work import AbstractPortfolioWork


class BaseImageWork(AbstractPortfolioWork):
    image_url = models.CharField(max_length=255)


class BaseAudiovisualWork(AbstractPortfolioWork):
    video_url = models.CharField(max_length=255)


class Photograph(BaseImageWork):
    class Meta:
        verbose_name = 'photograph'
        verbose_name_plural = 'photographs'
        db_table = 'photograph'


class Video(BaseAudiovisualWork):
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        db_table = 'video'
