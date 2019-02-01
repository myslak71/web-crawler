from requests_html import HTMLSession, HTML
import requests


def get_title_links(url):
    session = HTMLSession()

    try:
        response = session.get(url)
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
        return None

    response.html.render()
    title = response.html.find('title', first=True).text
    links = response.html.absolute_links
    print(links)
    links = {link for link in links if link.startswith(url)}
    return {'title': title, 'links': links}


def site_map(url):
    result = {url: get_title_links(url)}
    result_tmp = list(result[url]['links'])
    # for key, value in result.copy().items():
    #     urls = value['links']
    #     for url in urls:
    #         result[url] = get_title_links(url)
    #         print(url)
    for url in result_tmp.copy():
        if url in result:
            continue
        result[url] = get_title_links(url)
        result_tmp.remove(url)
        result_tmp.extend(result[url]['links'])
        print(result[url]['links'])
    print(result_tmp)
    return result


print(site_map('http://0.0.0.0:8000'))
