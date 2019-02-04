import pytest

from mock import Mock, patch
import responses

from web_crawler.site_map import *
from tests.fixtures.responses import *


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_no_links(mock_render):
    responses.add(responses.GET, 'http://0.0.0.0', body=body_no_links, status=200, content_type='text/html')
    assert site_map('http://0.0.0.0') == {'http://0.0.0.0': {'title': 'No links', 'links': set()}}


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_page_not_found(mock_render):
    responses.add(responses.GET, 'http://0.0.0.0', status=404, content_type='text/html')
    assert site_map('http://0.0.0.0') is None


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_invalid_content_type(mock_render):
    responses.add(responses.GET, 'http://0.0.0.0', status=200, content_type='text/plain')
    assert site_map('http://0.0.0.0') is None


@patch('requests_html.HTML.render')
@responses.activate
def test_site_map_one_empty_link(mock_render):
    responses.add(responses.GET, 'http://0.0.0.0', body=body_index_empty_link, status=200, content_type='text/html')
    responses.add(responses.GET, 'http://0.0.0.0/site', status=404)
    assert site_map('http://0.0.0.0') == {
        'http://0.0.0.0': {'links': {'http://0.0.0.0/site.html'}, 'title': 'Index empty link'}}

