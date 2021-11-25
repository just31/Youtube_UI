import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)

        if homepage_nav.is_visible('css', homepage_nav.popup_link_close, 'Close popup link on index page') is not None:
            homepage_nav.close_popup_index()

        number_links_header_menu = len(homepage_nav.get_nav_links())

        for indx in range(number_links_header_menu):
            homepage_nav.get_nav_links()[indx].click()

