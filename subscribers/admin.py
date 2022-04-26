from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import Subscribers


class SubscriberAdmin(ModelAdmin):
    model = Subscribers
    menu_label = "Subscribers"
    menu_icon = "placeholder"
    menu_order = 290
    list_display = ("email", "full_name")
    search_fields = ("email", "full_name")


modeladmin_register(SubscriberAdmin)
