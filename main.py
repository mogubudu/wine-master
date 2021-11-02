import datetime
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    this_year = datetime.datetime.now().year
    foundation_year = 1920
    winery_age = this_year - foundation_year

    wines = read_excel('wine3.xlsx', na_values='nan', keep_default_na=False)
    wines = wines.sort_values('Категория')
    wines = wines.to_dict(orient='record')

    grouped_wines = defaultdict(list)
    for wine in wines:
        (grouped_wines[wine['Категория']].append(wine))

    rendered_page = template.render(grouped_wines=grouped_wines,
                                    winery_age=winery_age)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
