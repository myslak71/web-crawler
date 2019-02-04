from argparse import ArgumentParser, RawDescriptionHelpFormatter

from web_crawler.site_map import site_map

description = """Description"""


def get_parser():
    parser = ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-u', '--url', help='Url to star crawl from', required=True)
    return parser


def main():
    parser = get_parser().parse_args()
    site_map(parser.url)


if __name__ == '__main__':
    main()
