Web Crawler
===========

[![Build Status](https://travis-ci.org/myslak71/web_crawler.svg?branch=master)](https://travis-ci.org/myslak71/web_crawler)
[![Coverage Status](https://coveralls.io/repos/github/myslak71/web_crawler/badge.svg?branch=master)](https://coveralls.io/github/myslak71/eb_crawler?branch=master)
![image](https://img.shields.io/badge/python-3.7-blue.svg)
### Description

Simple web crawling package.

Starts crawling from given domain_url. Visits every html link within specified domain
via HTTP/HTTPS, collects each site title and links and repeats the process for
collected links.

Returns dictionary of dictionaries as follows:

    {
        'http://0.0.0.0:8000': {
        'title': 'Index',
        'links': {'http://0.0.0.0:8000/example.html', 'http://0.0.0.0:8000/site.html'}
        }
        ...
    }



 
### Installation
```
git clone git+https://github.com/myslak71/web_crawler.git
```
```
pip install requirements.txt
```

Installing the package for CLI purposes
```
pip install git+https://github.com/myslak71/web_crawler.git

```

### Usage
In scripts:
```
site_map(url)
```

CLI:
 ```
 $ web-crawler --url URL
 ```
|OPTION    | |DESCRIPTION |
| --------  |---|-------------|
|-u, --url|REQUIRED |Domain URL to start crawling from|
|-h, --help|OPTIONAL |Help|
