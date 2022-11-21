from django.forms.utils import ErrorList
from wagtail.core import blocks
from wagtail.core.blocks.struct_block import StructBlockValidationError


class TextOnlyTeaserCard(blocks.StructBlock):

    heading = blocks.CharBlock(help_text="Heading for the card.")
    heading_link = blocks.PageChooserBlock(required=False, help_text="Page that the header should link out to.")
    link_url = blocks.CharBlock(
        required=False,
        help_text="Optional URL that the header should link out to.",
    )
    meta_data = blocks.CharBlock(max_length=500)
    body = blocks.TextBlock(help_text="Body text of the card.", required=False, max_length=200)

    def clean(self, value):
        result = super().clean(value)
        errors = {}

        if value["heading_link"] and value["link_url"]:
            errors["heading_link"] = ErrorList(["Please choose between a heading link OR a URL value."])
        if errors:
            raise StructBlockValidationError(errors)

        return result


class TextOnlyTeaserBlock(blocks.StructBlock):
    cards = blocks.ListBlock(TextOnlyTeaserCard(), help_text="Please use a minimum of 3 cards.", min_num=3)

    class Meta:
        icon = "placeholder"
        template = "wagtailpages/blocks/text_only_teaser_block.html"
