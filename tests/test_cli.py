import pytest

from argparse import Namespace
from mock import patch

from web_crawler.cli import main


@patch('web_crawler.cli.site_map')
@patch('web_crawler.cli.ArgumentParser.parse_args')
def test_cli(parse_args_mock, site_map_mock):
    parse_args_mock.return_value = Namespace(url='https://url')
    main()
    site_map_mock.assert_called_with('https://url')
