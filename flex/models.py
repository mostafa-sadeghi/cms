from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from streams import blocks


class Flexpage(Page):
    template = 'flex/flex_page.html'
    subtitle = models.CharField(max_length=100, blank=False, null=True)
    content = StreamField(
        [
         ('full_richtext', blocks.RichtextBlock()),
         ('simple_richtext', blocks.SimpleRichtextBlock()),
         ('title_and_text', blocks.TitleAndTextBlock()),
         ('card', blocks.CardBlock())
        ],
        null = True,
        blank = True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content')
    ]

    class Meta:
        verbose_name = "Flex صفحه"
        verbose_name_plural = "Flex pages"
