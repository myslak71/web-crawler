import requests
from requests_html import HTMLSession

from web_crawler.errors import InvalidContentType
from web_crawler.config import LOGGER

error_mapping = {
    'ConnectionError': 'Requested page was not found',
    'InvalidSchema': 'Invalid protocol, allowed HTTP and HTTPS',
    'InvalidContentType': 'Invalid Content-Type. Allowed text/html',
    'MissingSchema': 'Missing protocol, allowed HTTP and HTTPS',
    'InvalidURL': 'Invalid URL'
}


def site_map(domain_url):
    """
    Site crawling function.

    Starts crawling from given domain_url. Visits every html link within specified domain
    via HTTP/HTTPS and collects each site title and links.

    Returns dictionary of dictionaries in following format:
    {
        'http://0.0.0.0:8000': {
        'title': 'Index',
        'links': {'http://0.0.0.0:8000/example.html', 'http://0.0.0.0:8000/site.html'}
        }
        ...
    }

    :param domain_url:
        Valid url domain address
    :return:
        Dictionary containing url entries
    """
    try:
        url_entries = {domain_url: get_site_data(domain_url)}
    except Exception as error:
        LOGGER.error(error_mapping[error.__class__.__name__])
        return

    urls_to_visit = list(url_entries[domain_url]['links'])

    while urls_to_visit:
        for url in urls_to_visit.copy():
            if url in url_entries or not url.startswith(domain_url):
                urls_to_visit.remove(url)
                continue
            try:
                site_data = get_site_data(url)
            except Exception:
                urls_to_visit.remove(url)
                continue

            url_entries[url] = site_data
            urls_to_visit.extend(url_entries[url]['links'])

    LOGGER.info('URL ENTRIES:\n' + '\n'.join('{}\n\t{}'.format(url, entries) for url, entries in url_entries.items()))
    return url_entries


def get_site_data(url):
    """
    Fetches links and title from given url.

    If page response's Content-Type is not 'text/html', InvalidContentType is raised.

    If response's status code is 404, requests.exceptions.ConnectionError is raised

    :param url:
        Page url
    :return:
        Dictionary with two keys: 'title' and 'links'
    """
    session = HTMLSession()
    response = session.get(url)

    if not response.headers.get('Content-Type').startswith('text/html'):
        raise InvalidContentType(response.headers.get('Content-Type'))
    if response.status_code == 404:
        raise requests.exceptions.ConnectionError

    response.html.render()
    title = response.html.find('title', first=True).text
    return {'title': title, 'links': response.html.absolute_links}


# site_map('https://onet.pl')

# print(site_map('http://onet.pl'))
print(site_map('http://0.0.0.0:8000/'))

# session = HTMLSession()
# response = session.get('ftp://0.0.0.0:8000/text_file.txt')
# print(response)

#
# [dev-packages]
# mock = "*"
# responses = "*"
# pytest-cov = "*"
# coveralls = "*"
# pytest = "*"
#
# [packages]
# requests-html = "*"
# pyyaml = "*"
