import datetime
from http import HTTPStatus

from django import test
from django.core.handlers import wsgi
from django.utils import timezone

from networkapi.wagtailpages.tests import base as test_base
from networkapi.wagtailpages import models as pagemodels
from networkapi.wagtailpages.factory import buyersguide as buyersguide_factories


class BuyersGuideEditorialContentIndexPageFactoryTest(test_base.WagtailpagesTestCase):
    def test_factory(self):
        buyersguide_factories.BuyersGuideEditorialContentIndexPageFactory()


class BuyersGuideEditorialContentIndexPageTest(test_base.WagtailpagesTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.pni_homepage = buyersguide_factories.BuyersGuidePageFactory(
            parent=cls.homepage,
        )
        cls.content_index = buyersguide_factories.BuyersGuideEditorialContentIndexPageFactory(
            parent=cls.pni_homepage,
        )

    def create_request(self) -> wsgi.WSGIRequest:
        request_factory = test.RequestFactory()
        return request_factory.get(path=self.content_index.url)

    def test_parents(self):
        self.assertAllowedParentPageTypes(
            child_model=pagemodels.BuyersGuideEditorialContentIndexPage,
            parent_models={pagemodels.BuyersGuidePage},
        )

    def test_children(self):
        self.assertAllowedSubpageTypes(
            parent_model=pagemodels.BuyersGuideEditorialContentIndexPage,
            child_models={pagemodels.BuyersGuideArticlePage},
        )

    def test_page_success(self):
        response = self.client.get(self.content_index.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_template(self):
        # Needs to use the client to test the templates
        response = self.client.get(self.content_index.url)

        self.assertTemplateUsed(
            response=response,
            template_name='pages/buyersguide/editorial_content_index_page.html',
        )
        self.assertTemplateUsed(
            response=response,
            template_name='pages/buyersguide/base.html',
        )
        self.assertTemplateUsed(
            response=response,
            template_name='pages/base.html',
        )

    def test_children_titles_shown(self):
        children = []
        for _ in range(5):
            children.append(
                buyersguide_factories.BuyersGuideArticlePageFactory(
                    parent=self.content_index,
                )
            )

        response = self.content_index.serve(request=self.create_request())

        for child in children:
            self.assertContains(response=response, text=child.title, count=1)

    def test_get_items_ordered_by_publication_date(self):
        def create_days_old_article(days: int):
            return buyersguide_factories.BuyersGuideArticlePageFactory(
                parent=self.content_index,
                first_published_at=timezone.now() - datetime.timedelta(days=days),
            )

        article_middle = create_days_old_article(days=10)
        article_oldest = create_days_old_article(days=20)
        article_newest = create_days_old_article(days=5)

        result = self.content_index.get_items()

        self.assertQuerysetEqual(
            qs=result,
            values=[
                article_newest,
                article_middle,
                article_oldest,
            ],
            ordered=True,
        )

    def test_get_related_articles(self):
        content_index = self.content_index
        article1 = buyersguide_factories.BuyersGuideArticlePageFactory()
        article2 = buyersguide_factories.BuyersGuideArticlePageFactory()
        article3 = buyersguide_factories.BuyersGuideArticlePageFactory()
        buyersguide_factories.BuyersGuideEditorialContentIndexPageArticlePageRelationFactory(
            page=content_index,
            article=article2,
            sort_order=0,
        )
        buyersguide_factories.BuyersGuideEditorialContentIndexPageArticlePageRelationFactory(
            page=content_index,
            article=article1,
            sort_order=1,
        )
        buyersguide_factories.BuyersGuideEditorialContentIndexPageArticlePageRelationFactory(
            page=content_index,
            article=article3,
            sort_order=2,
        )

        related_articles = content_index.get_related_articles()

        self.assertEqual(len(related_articles), 3)
        self.assertListEqual(
            related_articles,
            [article2, article1, article3],
        )

    def test_featured_cta_in_context(self):
        featured_cta = buyersguide_factories.BuyersGuideCallToActionFactory()
        self.pni_homepage.call_to_action = featured_cta
        self.pni_homepage.save()

        context = self.content_index.get_context(request=self.create_request())

        self.assertEqual(context['featured_cta'], featured_cta)

    def test_context_with_no_home_page_cta_set(self):
        self.pni_homepage.call_to_action = None
        self.pni_homepage.save()

        context = self.content_index.get_context(request=self.create_request())

        self.assertIsNone(context['featured_cta'])
