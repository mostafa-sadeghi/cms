from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, help_text="facebook url")
    twitter = models.URLField(blank=True, null=True, help_text="twitter url")
    youtube = models.URLField(blank=True, null=True, help_text="youtube url")

    panels = [
        MultiFieldpanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ], heading="Social Media Settings")
    ]
