Web Crawler
===========

[![Build Status](https://travis-ci.org/myslak71/football_web_crawler.svg?branch=master)](https://travis-ci.org/myslak71/football_web_crawler)
[![Coverage Status](https://coveralls.io/repos/github/myslak71/football_web_crawler/badge.svg?branch=master)](https://coveralls.io/github/myslak71/football_web_crawler?branch=master)

### Description
Function allows to crawl from given domain, and collect visited sites'
titles and links within domain.



 
### Installation
```
git clone git+https://github.com/myslak71/web_crawler.git
```
```
pip install pipenv
```
```
pipenv install --dev
```

Installing the package for CLI purposes
```
pip install git+https://github.com/myslak71/web_crawler.git

```

### Usage
 ```
 $ web-crawler --url URL
 ```
|OPTION    | |DESCRIPTION |
| --------  |---|-------------|
|-u, --url|REQUIRED |Domain URL to start from|
|-h, --help|OPTIONAL |Help|
