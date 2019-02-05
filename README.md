Web Crawler
===========

[![Build Status](https://travis-ci.org/myslak71/web_crawler.svg?branch=master)](https://travis-ci.org/myslak71/web_crawler)
[![Coverage Status](https://coveralls.io/repos/github/myslak71/web_crawler/badge.svg?branch=master)](https://coveralls.io/github/myslak71/eb_crawler?branch=master)

### Description
Function allows to crawl from given domain, and collect visited sites'
titles and links within domain.



 
### Installation
```
git clone git+https://github.com/myslak71/web_crawler.git
```
```
pip install requirements-dev.txt
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
