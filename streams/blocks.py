from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="add title")
    text = blocks.TextBlock(required=True)

    class Meta:
        template = "streams/title_and_text.html"
        icon = "edit"
        label = "Title & Text"

class RichtextBlock(blocks.RichTextBlock):
    class Meta:
        template = 'streams/richtext_block.html'
        icon = "edit"
        label = "Full RichText"

class SimpleRichtextBlock(blocks.RichTextBlock):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.features = ["bold"]

    class Meta:
        template = 'streams/richtext_block.html'
        icon = "edit"
        label = "Simple RichText"