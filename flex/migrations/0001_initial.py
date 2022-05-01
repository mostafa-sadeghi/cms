# Generated by Django 4.0.4 on 2022-05-01 04:29

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flexpage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('content', wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichtextBlock()), ('simple_richtext', streams.blocks.SimpleRichtextBlock()), ('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', required=True)), ('text', wagtail.core.blocks.TextBlock(required=True))])), ('card', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='add title', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_lenght=40, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Flex صفحه',
                'verbose_name_plural': 'Flex pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
