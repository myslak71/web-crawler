import pytest

from mock import patch

from web_crawler.site_map import *
import responses

# class TestSiteMap(object):

@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps

# @patch('requests_html.HTMLSession.get')
# def test_api(mocked_responses):
#     mocked_responses.add(
#         responses.GET, 'http://twitter.com/api/1/foobar',
#         body='{<title>siema</title>}', status=200,
#         content_type='application/json')
#     res = get_site_data('http://twitter.com/api/1/foobar')
#     assert res == {'title': 'siema', 'links': set()}

    # @patch('requests_html.HTML.render', return_value="""
    #                                 <title>Page title</title>
    #                                 <a href="http://0.0.0.0:5000/link1.html>link1</a>
    #                                 <a href="/link1.html>link1</a>
    #                                 """)
    # def test_get_site_data(self, mocked_render):
    #     self.assertEqual(get_site_data('http://0.0.0.0:4000'),mocked_render())

