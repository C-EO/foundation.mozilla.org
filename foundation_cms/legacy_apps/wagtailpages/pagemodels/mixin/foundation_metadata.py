from taggit.models import Tag
from wagtail.images import get_image_model
from wagtailmetadata.models import MetadataPageMixin

default_social_share_tag = None
default_social_share_image = None
Image = get_image_model()


# Override the MetadataPageMixin to allow for a default
# description and image in page metadata for all Pages on the site
class FoundationMetadataPageMixin(MetadataPageMixin):
    def __init__(self, *args, **kwargs):
        # The first Wagtail image returned that has the specified tag name will
        # be the default image URL in social shares when no Image is specified at the Page level
        super().__init__(*args, **kwargs)

        # This will run once in the life-time of the server, when the first page instance
        # that inherits this mixin gets instantiated. After that, this code will not kick
        # in, and the default social share image is cached.
        if default_social_share_tag is None:
            self.set_default_social_share_tag_and_image()

    # Change this string to update the default description of all pages on the site
    default_description = (
        "Mozilla is a global non-profit dedicated to putting you in control of your online "
        "experience and shaping the future of the web for the public good. "
    )

    def get_meta_description(self):
        if self.search_description:
            return self.search_description

        parent = self.get_parent()

        while parent:
            if parent.search_description:
                return parent.search_description
            parent = parent.get_parent()

        return self.default_description

    def set_default_social_share_tag_and_image(self):
        # necessary because we're going to reassign them, rather than
        # assign same-named vars in local scope:
        global default_social_share_tag, default_social_share_image

        # get the tag with name "social share image"
        default_share_tag_name = "social share image"
        tag, create = Tag.objects.get_or_create(name=default_share_tag_name)
        default_social_share_tag = tag

        # then find an image in the CMS that uses that tag (defaulting to `None`):
        default_social_share_image = Image.objects.filter(tags=default_social_share_tag).first()

    def get_meta_image(self):
        # If we have a local social share image, use that
        if self.search_image:
            return self.search_image

        # If not, walk up our ancestor chain and use the first social
        # share image for an ancestor that explicitly has one set.
        parent = self.get_parent().specific
        while parent:
            if hasattr(parent, "search_image") and parent.search_image:
                return parent.search_image
            if hasattr(parent, "homepage") and parent.homepage.search_image:
                return parent.homepage.search_image
            parent = parent.get_parent()

        # We still haven't found a social share image, so, last resort: return
        # whatever is the default social share image. Which could be `None`!
        return default_social_share_image

    class Meta:
        abstract = True


# Overriding the name and help text for the FoundationMetadata's "search_image"
# field, which is found in the "Promote" tab of all pages that inherit this class.
# For more info see: https://learnwagtail.com/tutorials/customizing-default-property-values/
search_image_field = FoundationMetadataPageMixin._meta.get_field("search_image")
search_image_field.verbose_name = "Share Image"
search_image_field.help_text = (
    "Image must be high quality, include our logo mark and have the dimensions "
    "1200 x 628 px. For more design guidelines see here: "
    "https://foundation.mozilla.org/en/docs/brand/brand-identity/social-media/#og-images"
)
