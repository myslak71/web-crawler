import pytest

from mock import patch

from src.site_map import *
import responses


# class TestSiteMap(object):

@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps

def test_api(mocked_responses):
    mocked_responses.add(
        responses.GET, 'http://twitter.com/api/1/foobar',
        body='{}', status=200,
        content_type='application/json')
    resp = requests.get('http://twitter.com/api/1/foobar')
    print(resp)
    assert resp.status_code == 200

    # @patch('requests_html.HTML.render', return_value="""
    #                                 <title>Page title</title>
    #                                 <a href="http://0.0.0.0:5000/link1.html>link1</a>
    #                                 <a href="/link1.html>link1</a>
    #                                 """)
    # def test_get_site_data(self, mocked_render):
    #     self.assertEqual(get_site_data('http://0.0.0.0:4000'),mocked_render())
