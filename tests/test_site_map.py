import pytest

from mock import Mock, patch
from web_crawler.site_map import *
import responses

body = """
<head>
	<title>Test</title>
</head>
</html>
"""


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_no_links(mock_render):
    responses.add(responses.GET, 'http://0.0.0.0', body=body, status=200, content_type='text/html')
    assert site_map('http://0.0.0.0') == {'http://0.0.0.0': {'title': 'Test', 'links': set()}}


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_page_not_found(mock_render):
    responses.add(responses.GET, 'http://0.0.0.0', body=body, status=404, content_type='text/html')
    assert site_map('http://0.0.0.0') is None


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_invalid_content_type(mock_render):
    responses.add(responses.GET, 'http://0.0.0.0', body=body, status=200, content_type='text/plain')
    assert site_map('http://0.0.0.0') is None


# @patch('requests_html.HTML.render')
# @responses.activate
# def test_site_map(mock_render):
#     responses.add(responses.GET, 'http://0.0.0.0', body=body, status=200, content_type='text/plain')
#     assert site_map('http://0.0.0.0') is None
