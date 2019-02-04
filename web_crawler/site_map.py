from requests_html import HTMLSession
import requests
from web_crawler.errors import InvalidContentType
from web_crawler.config import LOGGER


def get_site_data(url):
    session = HTMLSession()
    response = session.get(url)
    if not response.headers.get('Content-Type').startswith('text/html'):
        raise InvalidContentType(response.headers.get('Content-Type'))
    if response.status_code == 404:
        raise requests.exceptions.ConnectionError
    response.html.render()

    title = response.html.find('title', first=True).text
    return {'title': title, 'links': response.html.absolute_links}


def site_map(domain_url):
    try:
        url_entries = {domain_url: get_site_data(domain_url)}
    except requests.exceptions.ConnectionError:
        LOGGER.error('Connection Error')
        return
    except requests.exceptions.InvalidSchema:
        LOGGER.error('Invalid protocol. Allowed HTTP and HTTPS')
        return
    except InvalidContentType as error:
        LOGGER.error(error)
        return
    except requests.exceptions.MissingSchema:
        LOGGER.error('Missing protocol. Allowed HTTP and HTTPS')
        return

    urls_to_visit = list(url_entries[domain_url]['links'])

    while urls_to_visit:
        for url in urls_to_visit.copy():
            if url in url_entries or not url.startswith(domain_url):
                urls_to_visit.remove(url)
                continue
            try:
                site_data = get_site_data(url)
            except requests.exceptions.ConnectionError:
                urls_to_visit.remove(url)
                continue
            except InvalidContentType:
                urls_to_visit.remove(url)
                continue

            url_entries[url] = site_data
            urls_to_visit.extend(url_entries[url]['links'])

    return url_entries


# print(site_map('http://onet.pl'))
# print(site_map('http://0.0.0.0:8000'))

# session = HTMLSession()
# response = session.get('ftp://0.0.0.0:8000/text_file.txt')
# print(response)
