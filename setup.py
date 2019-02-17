import os

from setuptools import setup, find_packages

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(DIR_PATH, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

requires = ['requests-html==0.9.0', 'pyyaml==3.13']

setup(
    name='web_crawler',
    version='1.0.0',
    packages=find_packages(exclude=('tests', 'example')),
    author='Kornel Szurek',
    author_email='kornel.szurek@protonmail.com',
    description='Web Crawler',
    long_description=long_description,
    install_requires=requires,
    python_requires=">=3.7",
    include_package_data=True,
    entry_points={
        'console_scripts': ['web-crawler=web_crawler.cli:main'],
    }
)
