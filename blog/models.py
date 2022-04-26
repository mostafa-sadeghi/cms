from django.db import models
from wagtail.core.models import Page


class BlogListingPage(Page):
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="override the default title"
    )

    def get_context(self, request, *args, **kwargs):
        """ """
        context = super().get_context(request, *args, **kwargs)
        return context


class BlogDetailPage(Page):
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="override the default title"
    )
    blog_image = models.ForeignKey(
        "wagtailimages", blank=False, null=False, related_name="+", on_delete=models.SET_NULL)
