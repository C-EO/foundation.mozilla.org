# Generated by Django 3.2.12 on 2022-03-29 20:16

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailpages", "0011_research_detail_page_main_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "paragraph",
                        wagtail.core.blocks.RichTextBlock(
                            features=[
                                "bold",
                                "italic",
                                "link",
                                "h2",
                                "h3",
                                "h4",
                                "h5",
                                "ol",
                                "ul",
                                "hr",
                                "document-link",
                            ],
                            template="wagtailpages/blocks/rich_text_block.html",
                        ),
                    ),
                    (
                        "card_grid",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "cards",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(),
                                                ),
                                                (
                                                    "alt_text",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Alt text for card's image.",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "title",
                                                    wagtail.core.blocks.CharBlock(help_text="Heading for the card."),
                                                ),
                                                (
                                                    "body",
                                                    wagtail.core.blocks.TextBlock(help_text="Body text of the card."),
                                                ),
                                                (
                                                    "link_url",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Optional URL that this card should link out to. (Note: If left blank, link will not render.) ",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "link_label",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Optional Label for the URL link above. (Note: If left blank, link will not render.) ",
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        ),
                                        help_text="Please use a minimum of 2 cards.",
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "image_grid",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "grid_items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(),
                                                ),
                                                (
                                                    "alt_text",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Alt text for this image.",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "caption",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Please remember to properly attribute any images we use.",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Optional URL that this figure should link out to.",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "square_image",
                                                    wagtail.core.blocks.BooleanBlock(
                                                        default=True,
                                                        help_text="If left checked, the image will be cropped to be square.",
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "iframe",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "url",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Please note that only URLs from allow-listed domains will work."
                                    ),
                                ),
                                (
                                    "height",
                                    wagtail.core.blocks.IntegerBlock(
                                        help_text="Optional integer pixel value for custom iFrame height",
                                        required=False,
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "captionURL",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Optional URL that this caption should link out to.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "iframe_width",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("normal", "Normal"),
                                            ("wide", "Wide"),
                                            ("full_width", "Full Width"),
                                        ],
                                        help_text="Wide iframes are col-12, Full-Width iframes reach both ends of the screen",
                                    ),
                                ),
                                (
                                    "disable_scroll",
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False,
                                        help_text='Checking this will add "scrolling=no" to the iframe. Use this if your iframe is rendering an unnecessary scroll bar or whitespace below it.',
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "image",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "altText",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Image description (for screen readers).",
                                        required=True,
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "captionURL",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Optional URL that this caption should link out to.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "image_width",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("normal", "Normal"),
                                            ("wide", "Wide"),
                                            ("full_width", "Full Width"),
                                        ],
                                        help_text="Wide images are col-12, Full-Width Images reach both ends of the screen (16:6 images recommended for full width)",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "audio",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("audio", wagtailmedia.blocks.AudioChooserBlock()),
                                (
                                    "caption",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "image_text",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "altText",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Image description (for screen readers).",
                                        required=True,
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.core.blocks.RichTextBlock(
                                        features=[
                                            "bold",
                                            "italic",
                                            "link",
                                            "h2",
                                            "h3",
                                            "h4",
                                            "h5",
                                            "ol",
                                            "ul",
                                            "hr",
                                            "document-link",
                                        ]
                                    ),
                                ),
                                (
                                    "url",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Optional URL that this image should link out to.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "top_divider",
                                    wagtail.core.blocks.BooleanBlock(
                                        help_text="Optional divider above content block.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "bottom_divider",
                                    wagtail.core.blocks.BooleanBlock(
                                        help_text="Optional divider below content block.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "image_text_mini",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "altText",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Image description (for screen readers).",
                                        required=True,
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.core.blocks.RichTextBlock(features=["bold", "italic", "link"]),
                                ),
                            ]
                        ),
                    ),
                    (
                        "video",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "url",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="For YouTube: go to your YouTube video and click “Share,” then “Embed,” and then copy and paste the provided URL only. For example: https://www.youtube.com/embed/3FIVXBawyQw For Vimeo: follow similar steps to grab the embed URL. For example: https://player.vimeo.com/video/9004979"
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "captionURL",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Optional URL for caption to link to.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "video_width",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("normal", "Normal"),
                                            ("wide", "Wide"),
                                            ("full_width", "Full Width"),
                                        ],
                                        help_text="Wide videos are col-12, Full-Width videos reach both ends of the screen.",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "linkbutton",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("label", wagtail.core.blocks.CharBlock()),
                                ("URL", wagtail.core.blocks.CharBlock()),
                                (
                                    "styling",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("btn-primary", "Primary button"),
                                            ("btn-secondary", "Secondary button"),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "looping_video",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "video_url",
                                    wagtail.core.blocks.CharBlock(
                                        help_text='Log into Vimeo using 1Password and upload the desired video. Then select the video and click "Advanced", "Distribution", and "Video File Links". Copy and paste the link here.'
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "pulse_listing",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "search_terms",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Test your search at mozillapulse.org/search",
                                        label="Search",
                                        required=False,
                                    ),
                                ),
                                (
                                    "max_number_of_results",
                                    wagtail.core.blocks.IntegerBlock(
                                        default=6,
                                        help_text="Choose 1-12. If you want visitors to see more, link to a search or tag on Pulse.",
                                        max_value=12,
                                        min_value=0,
                                        required=True,
                                    ),
                                ),
                                (
                                    "only_featured_entries",
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False,
                                        help_text="Featured items are selected by Pulse moderators.",
                                        label="Display only featured entries",
                                        required=False,
                                    ),
                                ),
                                (
                                    "newest_first",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("True", "Show newer entries first"),
                                            ("False", "Show older entries first"),
                                        ],
                                        label="Sort",
                                    ),
                                ),
                                (
                                    "advanced_filter_header",
                                    wagtail.core.blocks.static_block.StaticBlock(
                                        admin_text="-------- ADVANCED FILTERS: OPTIONS TO DISPLAY FEWER, MORE TARGETED RESULTS. --------",
                                        label=" ",
                                    ),
                                ),
                                (
                                    "issues",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("all", "All"),
                                            ("Decentralization", "Decentralization"),
                                            ("Digital Inclusion", "Digital Inclusion"),
                                            (
                                                "Online Privacy & Security",
                                                "Online Privacy & Security",
                                            ),
                                            ("Open Innovation", "Open Innovation"),
                                            ("Web Literacy", "Web Literacy"),
                                        ]
                                    ),
                                ),
                                (
                                    "help",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("all", "All"),
                                            ("Attend", "Attend"),
                                            ("Create content", "Create content"),
                                            ("Code", "Code"),
                                            ("Design", "Design"),
                                            ("Fundraise", "Fundraise"),
                                            ("Join community", "Join community"),
                                            (
                                                "Localize & translate",
                                                "Localize & translate",
                                            ),
                                            ("Mentor", "Mentor"),
                                            ("Plan & organize", "Plan & organize"),
                                            ("Promote", "Promote"),
                                            ("Take action", "Take action"),
                                            ("Test & feedback", "Test & feedback"),
                                            (
                                                "Write documentation",
                                                "Write documentation",
                                            ),
                                        ],
                                        label="Type of help needed",
                                    ),
                                ),
                                (
                                    "direct_link",
                                    wagtail.core.blocks.BooleanBlock(
                                        default=False,
                                        help_text="Checked: user goes to project link. Unchecked: user goes to pulse entry",
                                        label="Direct link",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "single_quote",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.core.blocks.RichTextBlock(features=["bold"]),
                                ),
                                (
                                    "attribution",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "attribution_info",
                                    wagtail.core.blocks.RichTextBlock(
                                        features=["bold", "link", "large"],
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "spacer",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "size",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("1", "quarter spacing"),
                                            ("2", "half spacing"),
                                            ("3", "single spacing"),
                                            ("4", "one and a half spacing"),
                                            ("5", "triple spacing"),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "airtable",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "url",
                                    wagtail.core.blocks.URLBlock(
                                        help_text="Copied from the Airtable embed code. The word 'embed' will be in the url"
                                    ),
                                ),
                                (
                                    "height",
                                    wagtail.core.blocks.IntegerBlock(
                                        default=533,
                                        help_text="The pixel height on desktop view, usually copied from the Airtable embed code",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "datawrapper",
                        wagtail.embeds.blocks.EmbedBlock(
                            help_text='Enter the "visualization only" link of the Datawrapper chart. It looks something like this: https://datawrapper.dwcdn.net/KwSKp/1/',
                            icon="image",
                            template="wagtailpages/blocks/datawrapper_block.html",
                        ),
                    ),
                    (
                        "typeform",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "embed_id",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="The embed id of your Typeform page (e.g. if the form is on admin.typeform.com/form/e8zScc6t, the id will be: e8zScc6t)",
                                        required=True,
                                    ),
                                ),
                                (
                                    "button_type",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("btn-primary", "Primary button"),
                                            ("btn-secondary", "Secondary button"),
                                        ]
                                    ),
                                ),
                                (
                                    "button_text",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="This is a text prompt for users to open the typeform content",
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
