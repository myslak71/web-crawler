import pytest

from mock import patch
import responses

from web_crawler.site_map import *
from tests.fixtures.responses import *


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_no_links(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', body=body_no_links, status=200, content_type='text/html')
    assert site_map('http://0.0.0.0') == {'http://0.0.0.0': {'title': 'No links', 'links': set()}}


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_page_not_found(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', status=404, content_type='text/html')
    assert site_map('http://0.0.0.0') is None


@patch('requests_html.HTML.render')
@responses.activate
def test_get_site_data_invalid_content_type(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', status=200, body=body_no_links, content_type='text/plain')
    assert site_map('http://0.0.0.0') is None


def test_site_map_no_url():
    assert site_map('') is None


def test_site_map_invalid_schema():
    assert site_map('ftp://0.0.0.0') is None


@patch('requests_html.HTML.render')
@responses.activate
def test_site_map_external_link(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', status=200, body=body_index_external_link, content_type='text/html')
    assert site_map('http://0.0.0.0') == {
        'http://0.0.0.0': {'links': {'http://clearcode.pl'}, 'title': 'External Link'}}


@patch('requests_html.HTML.render')
@responses.activate
def test_site_map_link_to_index(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', status=200, body=body_index_redirects, content_type='text/html')
    responses.add(responses.GET, 'http://0.0.0.0/site_redirects.html', status=200, body=body_site_redirects,
                  content_type='text/html')
    assert site_map('http://0.0.0.0') == {
        'http://0.0.0.0': {'links': {'http://0.0.0.0/site_redirects.html'}, 'title': 'External Link'},
        'http://0.0.0.0/site_redirects.html': {
            'links': {'http://0.0.0.0', 'http://0.0.0.0/subsite.html', 'http://clearcode.pl'},
            'title': 'Site links to index'}}


@patch('requests_html.HTML.render')
@responses.activate
def test_site_map_invalid_link(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', status=200, body=body_index_site_link, content_type='text/html')
    responses.add(responses.GET, 'http://0.0.0.0/site.html', status=200, body=body_site_invalid_link,
                  content_type='text/html')
    responses.add(responses.GET, 'http://0.0.0.0/invalid_link.html', status=404,
                  content_type='text/html')
    assert site_map('http://0.0.0.0') == {'http://0.0.0.0': {'title': 'Test', 'links': {'http://0.0.0.0/site.html'}},
                                          'http://0.0.0.0/site.html': {'title': 'Invalid link',
                                                                       'links': {'http://0.0.0.0/invalid_link.html'}}}


@patch('requests_html.HTML.render')
@responses.activate
def test_site_map_invalid_link_content(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', status=200, body=body_index_site_link, content_type='text/html')
    responses.add(responses.GET, 'http://0.0.0.0/site.html', status=200, body=body_site_invalid_content_link,
                  content_type='text/html')
    responses.add(responses.GET, 'http://0.0.0.0/invalid_content.txt', status=200, body='Invalid content',
                  content_type='text/plain')
    assert site_map('http://0.0.0.0') == {'http://0.0.0.0': {'title': 'Test', 'links': {'http://0.0.0.0/site.html'}},
                                          'http://0.0.0.0/site.html': {'title': 'Invalid link',
                                                                       'links': {'http://0.0.0.0/invalid_content.txt'}}}


@patch('requests_html.HTML.render')
@responses.activate
def test_site_map_one_empty_link(render_mock):
    responses.add(responses.GET, 'http://0.0.0.0', body=body_index_empty_link, status=200, content_type='text/html')
    responses.add(responses.GET, 'http://0.0.0.0/site', status=404)
    assert site_map('http://0.0.0.0') == {
        'http://0.0.0.0': {'links': {'http://0.0.0.0/site.html'}, 'title': 'Index empty link'}}

@responses.activate
def test_get_site_data_invalid_status_code():
    responses.add(responses.GET, 'http://0.0.0.0/err', status=300, content_type='text/html', body="asdas")
    with pytest.raises(requests.exceptions.ConnectionError) as error:
        get_site_data('http://0.0.0.0/err')
