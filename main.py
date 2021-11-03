import datetime
import argparse


from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path_to_file',
        '-ptf',
        default='',
        help='Specify the full path to the directory where your file is located')
    parser.add_argument(
        '--file_name',
        '-f',
        default='wine.xlsx',
        help='You can specify the name of the file with data. The name is specified together with the file type (only .xlsx)'
    )
    return parser

def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    this_year = datetime.datetime.now().year
    foundation_year = 1920
    winery_age = this_year - foundation_year

    parser = create_parser()
    parser_namespace = parser.parse_args()
    path_to_file = parser_namespace.path_to_file
    file_name = parser_namespace.file_name

    wines = read_excel(f'{path_to_file}{file_name}', na_values='nan', keep_default_na=False)
    wines = wines.sort_values('Категория')
    wines = wines.to_dict(orient='record')

    grouped_wines = defaultdict(list)
    for wine in wines:
        grouped_wines[wine['Категория']].append(wine)

    rendered_page = template.render(grouped_wines=grouped_wines,
                                    winery_age=winery_age)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
