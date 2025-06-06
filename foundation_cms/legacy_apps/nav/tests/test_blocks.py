import wagtail_factories
from django.test import TestCase
from wagtail.blocks import StreamBlockValidationError, StructBlockValidationError
from wagtail.models import Locale, Page

from foundation_cms.legacy_apps.nav import blocks as nav_blocks
from foundation_cms.legacy_apps.nav import factories as nav_factories
from foundation_cms.legacy_apps.wagtailpages.factory.image_factory import ImageFactory


class TestNavItemBlock(TestCase):
    def test_default(self):
        """Assert that default nav_blocks.NavItem factory works and is an external URL."""
        block = nav_factories.NavItemFactory()

        # Assert that the page link is custom URL and that it is correct
        url = block["external_url"]
        self.assertEqual(block.url, url)

    def test_page_link(self):
        """Create a nav_blocks.NavItem with a page link."""
        block = nav_factories.NavItemFactory(page_link=True)

        page = block["page"]
        self.assertIsNotNone(page)
        self.assertTrue(isinstance(page, Page))
        default_locale = Locale.get_default()
        self.assertEqual(page.locale, default_locale)

        self.assertFalse(block.is_external)

        # Assert that other fields are empty
        self.assertEqual(block["external_url"], "")
        self.assertEqual(block["relative_url"], "")

    def test_external_url_link(self):
        """Create a nav_blocks.NavItem with a custom/external URL."""
        block = nav_factories.NavItemFactory(external_url_link=True)

        # Assert that the URL is a URL
        url = block["external_url"]
        self.assertIsNotNone(url)

        self.assertTrue(block.is_external)

        # Assert that other fields are empty
        self.assertIsNone(block["page"])
        self.assertEqual(block["relative_url"], "")

    def test_relative_url_link(self):
        """Create a nav_blocks.NavItem with a relative URL."""
        block = nav_factories.NavItemFactory(relative_url_link=True)

        # Assert that the URL is a URL
        url = block["relative_url"]
        self.assertIsNotNone(url)

        self.assertFalse(block.is_external)

        # Assert that other fields are empty
        self.assertIsNone(block["page"])
        self.assertEqual(block["external_url"], "")

    def test_needs_to_provide_at_least_one_link(self):
        with self.assertRaises(StreamBlockValidationError):
            block = nav_factories.NavItemFactory()
            nav_blocks.NavItem().clean(block)


class TestNavFeaturedItemBlock(TestCase):
    def test_default(self):
        """Assert that default nav_blocks.NavFeaturedItem factory works and is an external URL."""
        block = nav_factories.NavFeaturedItemFactory()

        # Assert that the page link is custom URL and that it is correct
        url = block["external_url"]
        self.assertEqual(block.url, url)
        self.assertTrue(block.is_external)

    def test_valid_svg_upload(self):
        """Test that an SVG file is accepted by the NavFeaturedItem model."""

        # Create an image instance using the SVG format.
        svg_image = ImageFactory(file__filename="icon.svg", file__extension="svg")

        # Return a list of block data with the NavFeaturedItem factory, using the SVG image for "icon".
        block_data = nav_factories.NavFeaturedItemFactory(icon=svg_image, external_url_link=True)

        # Use the NavFeaturedItem model's clean() method to see if any validation errors are returned.
        try:
            nav_blocks.NavFeaturedItem().clean(block_data)
        except StructBlockValidationError:
            # We are expecting no errors. If one arrises, fail this test to let us know something is wrong.
            self.fail("Clean method raised StructBlockValidationError unexpectedly")

    def test_invalid_svg_upload(self):
        """Test that a non-SVG file is not accepted by the NavFeaturedItem model."""

        # Create an image instance using the JPEG format.
        jpeg_image = ImageFactory(file__filename="icon.jpeg", file__extension="jpeg")

        # Return a list of block data with the NavFeaturedItem factory, using the JPEG image for "icon".
        block_data = nav_factories.NavFeaturedItemFactory(icon=jpeg_image, external_url_link=True)

        # Use the NavFeaturedItem model's clean() method to see if any validation errors are returned.
        with self.assertRaises(StructBlockValidationError) as context:
            nav_blocks.NavFeaturedItem().clean(block_data)

        # Expecting 1 validation error, related to "icon".
        self.assertIn("icon", context.exception.block_errors)
        self.assertEqual(len(context.exception.block_errors), 1)


class TestNavButton(TestCase):
    def test_default(self):
        """Assert that default nav_blocks.NavButton factory works and is an external URL."""
        block = nav_factories.NavButtonFactory()

        # Assert that the page link is custom URL and that it is correct
        url = block["external_url"]
        self.assertEqual(block.url, url)

    def test_page_link(self):
        """Create a nav_blocks.NavButton with a page link."""
        block = nav_factories.NavButtonFactory(page_link=True)

        page = block["page"]
        self.assertIsNotNone(page)
        self.assertTrue(isinstance(page, Page))
        default_locale = Locale.get_default()
        self.assertEqual(page.locale, default_locale)

        # Assert that other fields are empty
        self.assertEqual(block["external_url"], "")
        self.assertEqual(block["relative_url"], "")

    def test_external_url_link(self):
        """Create a nav_blocks.NavButton with a custom/external URL."""
        block = nav_factories.NavButtonFactory(external_url_link=True)

        # Assert that the URL is a URL
        url = block["external_url"]
        self.assertIsNotNone(url)

        # Assert that other fields are empty
        self.assertIsNone(block["page"])
        self.assertEqual(block["relative_url"], "")

    def test_relative_url_link(self):
        """Create a nav_blocks.NavButton with a relative URL."""
        block = nav_factories.NavButtonFactory(relative_url_link=True)

        # Assert that the URL is a URL
        url = block["relative_url"]
        self.assertIsNotNone(url)

        # Assert that other fields are empty
        self.assertIsNone(block["page"])
        self.assertEqual(block["external_url"], "")

    def test_needs_to_provide_at_least_one_link(self):
        with self.assertRaises(StreamBlockValidationError):
            block = nav_factories.NavItemFactory()
            nav_blocks.NavItem().clean(block)


class TestNavColumnBlock(TestCase):
    def test_default(self):
        """Assert that default nav_blocks.NavColumn factory works and is an external URL."""
        block = nav_factories.NavColumnFactory()

        self.assertEqual(len(block["nav_items"]), 4)
        for link in block["nav_items"]:
            self.assertIsInstance(link.block, nav_blocks.NavItem)
            self.assertIsInstance(link, nav_blocks.NavItemValue)
        self.assertIsNotNone(block.button_value)
        self.assertEqual(len(block["button"]), 1)
        self.assertEqual(block.button_value, block["button"][0])
        self.assertTrue(block.has_button)

    def test_without_button(self):
        """Create a nav_blocks.NavColumn without a button."""
        block = nav_factories.NavColumnFactory(no_button=True)

        self.assertEqual(len(block["button"]), 0)
        self.assertFalse(block.has_button)
        self.assertIsNone(block.button_value)

    def test_with_variable_number_of_links(self):
        """Create a nav_blocks.NavColumn with links."""
        block = nav_factories.NavColumnFactory(
            **{
                "nav_items__0__page_url_link": True,
                "nav_items__1__relative_url_link": True,
                "nav_items__2__external_url_link": True,
            }
        )

        self.assertEqual(len(block["nav_items"]), 4)
        for link in block["nav_items"]:
            self.assertIsInstance(link.block, nav_blocks.NavItem)
            self.assertIsInstance(link, nav_blocks.NavItemValue)

    def test_needs_to_provide_at_least_one_link(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavColumnFactory(nav_items=[])
            nav_blocks.NavColumn().clean(block)

    def test_needs_to_provide_at_most_four_links(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavColumnFactory(
                **{
                    "nav_items__0__external_url_link": True,
                    "nav_items__1__external_url_link": True,
                    "nav_items__2__external_url_link": True,
                    "nav_items__3__external_url_link": True,
                    "nav_items__4__external_url_link": True,
                }
            )
            nav_blocks.NavColumn().clean(block)

    def test_cannot_have_more_than_one_button(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavColumnFactory(
                **{
                    "button__0__external_url_link": True,
                    "button__1__external_url_link": True,
                }
            )
            nav_blocks.NavColumn().clean(block)


class TestNavFeaturedColumnBlock(TestCase):
    def test_default(self):
        """Assert that default nav_blocks.NavFeaturedColumn factory works and is an external URL."""
        block = nav_factories.NavFeaturedColumnFactory()

        self.assertEqual(len(block["nav_items"]), 4)
        for link in block["nav_items"]:
            self.assertIsInstance(link.block, nav_blocks.NavFeaturedItem)
            self.assertIsInstance(link, nav_blocks.NavItemValue)

    def test_with_variable_number_of_links(self):
        """Create a nav_blocks.NavFeaturedColumn with links."""
        block = nav_factories.NavFeaturedColumnFactory(
            **{
                "nav_items__0__page_url_link": True,
                "nav_items__1__relative_url_link": True,
                "nav_items__2__external_url_link": True,
            }
        )

        self.assertEqual(len(block["nav_items"]), 4)
        for link in block["nav_items"]:
            self.assertIsInstance(link.block, nav_blocks.NavFeaturedItem)
            self.assertIsInstance(link, nav_blocks.NavItemValue)

    def test_needs_to_provide_at_least_one_link(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavFeaturedColumnFactory(nav_items=[])
            nav_blocks.NavFeaturedColumn().clean(block)

    def test_needs_to_provide_at_most_four_links(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavFeaturedColumnFactory(
                **{
                    "nav_items__0__external_url_link": True,
                    "nav_items__1__external_url_link": True,
                    "nav_items__2__external_url_link": True,
                    "nav_items__3__external_url_link": True,
                    "nav_items__4__external_url_link": True,
                }
            )
            nav_blocks.NavFeaturedColumn().clean(block)


class TestNavDropdownBlock(TestCase):
    def test_default_block_factory(self):
        """Default factory creates a block with 4 columns and a button"""
        block = nav_factories.NavDropdownFactory()
        nav_blocks.NavDropdown().clean(block)

        self.assertEqual(len(block["overview"]), 0)
        self.assertFalse(block.has_overview)
        self.assertIsNone(block.overview_value)

        self.assertEqual(len(block["columns"]), 4)
        for column in block["columns"]:
            self.assertIsInstance(column.block, nav_blocks.NavColumn)
            self.assertIsInstance(column, nav_blocks.NavColumnValue)

        self.assertEqual(len(block["featured_column"]), 0)
        self.assertFalse(block.has_featured_column)
        self.assertIsNone(block.featured_column_value)

        self.assertTrue(block["button"])
        self.assertIsInstance(block["button"].block, nav_blocks.NavButton)

        self.assertEqual(block.ncols, 4)

    def test_block_with_overview(self):
        """Create a nav_blocks.NavDropdown with an overview."""
        block = nav_factories.NavDropdownFactory(with_overview=True)
        nav_blocks.NavDropdown().clean(block)

        self.assertEqual(len(block["overview"]), 1)
        self.assertTrue(block.has_overview)
        self.assertEqual(block.overview_value, block["overview"][0])

        self.assertEqual(len(block["columns"]), 3)

        self.assertEqual(block.ncols, 4)

    def test_block_with_featured_column(self):
        """Create a nav_blocks.NavDropdown with a featured column."""
        block = nav_factories.NavDropdownFactory(with_featured_column=True)
        nav_blocks.NavDropdown().clean(block)

        self.assertEqual(len(block["featured_column"]), 1)
        self.assertTrue(block.has_featured_column)
        self.assertEqual(block.featured_column_value, block["featured_column"][0])

        self.assertEqual(len(block["columns"]), 3)

        self.assertEqual(block.ncols, 4)

    def test_block_with_overview_and_featured_column(self):
        """Create a nav_blocks.NavDropdown with an overview and a featured column."""
        block = nav_factories.NavDropdownFactory(with_overview_and_featured_column=True)
        nav_blocks.NavDropdown().clean(block)

        self.assertEqual(len(block["overview"]), 1)
        self.assertTrue(block.has_overview)
        self.assertEqual(block.overview_value, block["overview"][0])

        self.assertEqual(len(block["featured_column"]), 1)
        self.assertTrue(block.has_featured_column)
        self.assertEqual(block.featured_column_value, block["featured_column"][0])

        self.assertEqual(len(block["columns"]), 2)

        self.assertEqual(block.ncols, 4)

    def test_number_of_cols_prop(self):
        """Test the number of columns property."""
        block = nav_factories.NavDropdownFactory()
        nav_blocks.NavDropdown().clean(block)

        self.assertEqual(block.ncols, 4)

        block = nav_factories.NavDropdownFactory(
            columns=wagtail_factories.ListBlockFactory(
                nav_factories.NavColumnFactory,
                **{
                    "0__title": "Column 1",
                    "1__title": "Column 2",
                },
            ),
        )
        nav_blocks.NavDropdown().clean(block)
        self.assertEqual(block.ncols, 2)

        block = nav_factories.NavDropdownFactory(
            columns=wagtail_factories.ListBlockFactory(
                nav_factories.NavColumnFactory,
                **{
                    "0__title": "Column 1",
                    "1__title": "Column 2",
                    "2__title": "Column 3",
                },
            ),
        )
        nav_blocks.NavDropdown().clean(block)
        self.assertEqual(block.ncols, 3)

        block = nav_factories.NavDropdownFactory(
            columns=wagtail_factories.ListBlockFactory(
                nav_factories.NavColumnFactory,
                **{
                    "0__title": "Column 1",
                    "1__title": "Column 2",
                    "2__title": "Column 3",
                    "3__title": "Column 4",
                },
            ),
        )
        nav_blocks.NavDropdown().clean(block)
        self.assertEqual(block.ncols, 4)

    def test_cannot_have_block_without_button(self):
        """Cannot create a nav_blocks.NavDropdown without a button."""
        # Here it raises an attribute error because it assumes that a button will be present
        with self.assertRaises(AttributeError):
            block = nav_factories.NavDropdownFactory(button=None)
            nav_blocks.NavDropdown().clean(block)

    def test_needs_at_least_one_column(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavDropdownFactory(columns=[])
            nav_blocks.NavDropdown().clean(block)

    def test_cannot_have_more_than_four_columns(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavDropdownFactory(
                **{
                    "columns__0__title": "Column 1",
                    "columns__1__title": "Column 2",
                    "columns__2__title": "Column 3",
                    "columns__3__title": "Column 4",
                    "columns__4__title": "Column 5",
                }
            )
            nav_blocks.NavDropdown().clean(block)

    def test_block_with_overview_cannot_have_more_than_three_columns(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavDropdownFactory(
                **{
                    "overview__0__title": "Overview",
                    "columns__0__title": "Column 1",
                    "columns__1__title": "Column 2",
                    "columns__2__title": "Column 3",
                    "columns__3__title": "Column 4",
                }
            )
            nav_blocks.NavDropdown().clean(block)

    def test_block_with_featured_column_cannot_have_more_than_three_columns(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavDropdownFactory(
                **{
                    "columns__0__title": "Column 1",
                    "columns__1__title": "Column 2",
                    "columns__2__title": "Column 3",
                    "columns__3__title": "Column 4",
                    "featured_column__0__title": "Featured column",
                }
            )
            nav_blocks.NavDropdown().clean(block)

    def test_block_with_featured_column_and_overview_cannot_have_more_than_two_columns(self):
        with self.assertRaises(StructBlockValidationError):
            block = nav_factories.NavDropdownFactory(
                **{
                    "overview__0__title": "Overview",
                    "columns__0__title": "Column 1",
                    "columns__1__title": "Column 2",
                    "columns__2__title": "Column 3",
                    "featured_column__0__title": "Featured column",
                }
            )
            nav_blocks.NavDropdown().clean(block)
