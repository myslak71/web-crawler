from requests_html import HTMLSession
import requests


def get_site_data(url, domain_url=0):
    session = HTMLSession()
    response = session.get(url)

    if response.status_code == 404:
        raise requests.exceptions.ConnectionError

    if domain_url == 0:
        domain_url = url

    response.html.render()
    title = response.html.find('title', first=True).text
    links = response.html.absolute_links
    links = {link for link in links if link.startswith(domain_url)}

    return {'title': title, 'links': links}


def site_map(domain_url):
    try:
        result = {domain_url: get_site_data(domain_url)}
    except requests.exceptions.ConnectionError:
        return ('Connection Error')

    result_tmp = list(result[domain_url]['links'])

    while True:
        for url in result_tmp.copy():
            if url in result:
                result_tmp.remove(url)
                continue

            try:
                site_data = get_site_data(url, domain_url)
            except requests.exceptions.ConnectionError:
                result_tmp.remove(url)
                continue

            result[url] = site_data
            result_tmp.extend(result[url]['links'])
        if not result_tmp:
            break
    return result


print(site_map('http://0.0.0.0:8000'))
