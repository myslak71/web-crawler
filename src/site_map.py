from requests_html import HTMLSession, HTML
import requests


def get_title_links(url, domain_url=0):
    session = HTMLSession()

    try:
        response = session.get(url)
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
        return None

    if domain_url == 0:
        domain_url = url
    response.html.render()
    title = response.html.find('title', first=True).text
    links = response.html.absolute_links
    links = {link for link in links if link.startswith(domain_url)}
    return {'title': title, 'links': links}


def site_map(domain_url):
    result = {domain_url: get_title_links(domain_url)}
    result_tmp = list(result[domain_url]['links'])
    while True:
        for url in result_tmp.copy():
            if url in result:
                result_tmp.remove(url)
                continue
            result[url] = get_title_links(url, domain_url)
            result_tmp.extend(result[url]['links'])
        print(result_tmp)
        if result_tmp == []:
            break
    return result


print(site_map('http://0.0.0.0:8000'))

