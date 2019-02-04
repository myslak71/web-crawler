from argparse import ArgumentParser, RawDescriptionHelpFormatter

from web_crawler.site_map import site_map


description = """Description"""

def get_parser():
    parser = ArgumentParser(description=description, formatter_class=RawDescriptionHelpFormatter)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-u', '--url', help='Input CSV file path', required=True)
    return parser


def main():
    parser = get_parser().parse_args()

    processer = ReportProcesser()
    processer.process_csv_report(parser.input, parser.output, parser.errors)


if __name__ == '__main__':
    main()
