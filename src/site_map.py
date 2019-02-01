from requests_html import HTMLSession, HTML
import requests






def site_map(url, result=[]):
    session = HTMLSession()
    try:
        response = session.get(url)
    except requests.exceptions.ConnectionError:
        print('blad')
        return None
    response.html.render()
    print(response.html.links)


site_map('http://0.0.0.0:8000')
