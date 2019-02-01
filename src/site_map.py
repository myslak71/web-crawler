from requests_html import HTMLSession
import requests


def get_site_data(url, **kwargs):
    session = HTMLSession()
    response = session.get(url)

    if response.status_code == 404:
        raise requests.exceptions.ConnectionError

    if not kwargs.get('domain'):
        domain_url = url
    else:
        domain_url = kwargs.get('domain')

    response.html.render()
    title = response.html.find('title', first=True).text
    links = response.html.absolute_links
    links = {link for link in links if link.startswith(domain_url)}

    return {'title': title, 'links': links}


def site_map(domain_url):
    try:
        url_entries = {domain_url: get_site_data(domain_url)}
    except requests.exceptions.ConnectionError:
        return ('Connection Error')

    urls_to_visit = list(url_entries[domain_url]['links'])

    while True:
        for url in urls_to_visit.copy():
            if url in url_entries:
                urls_to_visit.remove(url)
                continue

            try:
                site_data = get_site_data(url, domain=domain_url)
            except requests.exceptions.ConnectionError:
                urls_to_visit.remove(url)
                continue

            url_entries[url] = site_data
            urls_to_visit.extend(url_entries[url]['links'])
        if not urls_to_visit:
            break
    return url_entries


print(site_map('http://0.0.0.0:8000'))
