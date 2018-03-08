from django.utils import timezone
from django.db import models


class Article(models.Model):
    """A self-contained purely written content which can be written, stored
    and published by an user. Its principal components are a title, subtitle and
    the main content.
    """
    title = models.CharField(max_length=255, default='Article Title',
                             help_text="A title for the article.")
    subtitle = models.CharField(null=True, blank=True, max_length=255,
                                help_text="A quick description of the article to make it "
                                          "compelling for other users to read it. Maximum "
                                          "of 255 characters.")
    content = models.TextField(default='Lorem ipsum sit dolor amet.',
                               help_text="Your article content.")

    # TODO: Add author field pointing to the User model once accounts and
    # authentication are implemented.

    # Datetime records
    created_at = models.DateTimeField(default=timezone.now, editable=False,
                                      help_text="The initial time the article has been "
                                                "created.")
    published_at = models.DateTimeField(null=True,
                                        help_text="The timestamp when the article was "
                                                  "first published.")

    # TODO: Add AuditLog here. This is the main reason why there's no timestamp
    # for the editions here.
