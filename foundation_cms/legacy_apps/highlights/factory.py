from datetime import timezone

from factory import Faker, LazyAttribute, Trait, post_generation
from factory.django import DjangoModelFactory

from foundation_cms.legacy_apps.highlights.models import Highlight
from foundation_cms.legacy_apps.utility.faker import generate_fake_data
from foundation_cms.legacy_apps.utility.faker.helpers import reseed
from foundation_cms.legacy_apps.wagtailpages.factory.image_factory import ImageFactory


class HighlightFactory(DjangoModelFactory):
    class Meta:
        model = Highlight
        exclude = (
            "title_sentence",
            "link_label_words",
            "footer_sentence",
        )

    class Params:
        unpublished = Trait(publish_after=Faker("future_datetime", end_date="+30d", tzinfo=timezone.utc))
        has_expiry = Trait(expires=Faker("future_datetime", end_date="+30d", tzinfo=timezone.utc))
        expired = Trait(expires=Faker("past_datetime", start_date="-30d", tzinfo=timezone.utc))

    title = LazyAttribute(lambda o: o.title_sentence.rstrip("."))
    description = Faker("paragraph", nb_sentences=5, variable_nb_sentences=True)
    link_label = LazyAttribute(lambda o: " ".join(o.link_label_words))
    footer = LazyAttribute(lambda o: o.footer_sentence.rstrip("."))
    link_url = Faker("uri")
    publish_after = Faker("past_datetime", start_date="-30d", tzinfo=timezone.utc)
    expires = None
    order = 0

    # LazyAttribute helper values
    title_sentence = Faker("sentence", nb_words=4)
    link_label_words = Faker("words", nb=3)
    footer_sentence = Faker("sentence", nb_words=5)

    @post_generation
    def image_name(self, create, extracted, **kwargs):
        self.image = ImageFactory()


def generate(seed):
    reseed(seed)

    print("Generating Highlights")
    generate_fake_data(HighlightFactory, 10)
