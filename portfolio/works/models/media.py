from django.db import models
from .work import AbstractPortfolioWork


class BaseImageWork(AbstractPortfolioWork):
    image_url = models.CharField(max_lenght=255)


class BaseAudiovisualWork(AbstractPortfolioWork):
    pass


class Photograph(BaseImageWork):
    pass


class Video(BaseAudiovisualWork):
    pass
