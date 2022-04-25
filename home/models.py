from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePageCarouselImages(Orderable):
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey("wagtailimages.Image",
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       related_name="+"
                                       )
    panels = [
        ImageChooserPanel("carousel_image"),
    ]


class HomePage(Page):
    template = "home/home_page.html"
    # max_count = 1
    banner_title = models.CharField(max_length=100, blank=True, null=True)
    banner_subtitle = RichTextField(
        features=["bold", "italic"], blank=False, null=True)
    banner_image = models.ForeignKey("wagtailimages.Image",
                                     null=True,
                                     blank=False,
                                     on_delete=models.SET_NULL,
                                     related_name='+'
                                     )
    banner_cta = models.ForeignKey("wagtailcore.Page",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name='+')
    content_panels = Page.content_panels + [
        MultiFieldPanel([

            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading="banner options"),
        MultiFieldPanel([

            InlinePanel("carousel_images", max_num=5, min_num=1, label="image")
        ], heading="Carousel Image")

    ]

    class Meta:
        verbose_name = "Home page"
        verbose_name_plural = "Home pages"
