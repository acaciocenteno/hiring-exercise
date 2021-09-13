import os
import sys
from datetime import datetime, timedelta

import click
from tabulate import tabulate

DATE_FORMAT = "%Y-%m-%d"

class SellingTransaction(object):
    def __init__(self, date, sku, volume, price):
        self.date = date
        self.sku = sku
        self.volume = volume
        self.price = price

    def revenue(self):
        return self.volume * self.price

def parse_line_to_object(line):
    components = line.split(' ')
    real_components = []
    for component in components:
        if component != '':
            real_components.append(component)
    components = real_components

    date   = components[0]
    sku    = int(components[1])
    volume = int(components[2])
    price  = int(components[3])
    return SellingTransaction(date, sku, volume, price)

def calculate_totals(path,
                     start,
                     end):
    # Naive implementation. Please comment on code smells and problems.
    summary = {}

    try:
        start = datetime.strptime(start, DATE_FORMAT).date()
        end = datetime.strptime(end, DATE_FORMAT).date()

        input_file = open(path, 'r')
        for line in input_file.readlines():
            trn = parse_line_to_object(line)
            trn_date = datetime.strptime(trn.date, DATE_FORMAT).date()
            if start <= trn_date <= end:
                if trn.sku not in summary:
                    summary[trn.sku] = trn.revenue() / 100.
                else:
                    summary[trn.sku] += trn.revenue() / 100.

        top_ten = []

        for sku in summary:
            revenue = summary[sku]
            if len(top_ten) < 10:
                top_ten = top_ten + [(sku, revenue)]
            else:
                i=0
                for i in range(9, -1, -1):  # xrange(9, -1, -1)
                    if revenue <= top_ten[i][1]:
                        break
                if i>=0 and i < 9:
                    top_ten = top_ten[:i] + [(sku, revenue)] + top_ten[i+1:]
                # top_ten = top_ten[0:10]

    except IOError as e:
        print(f'Could not read path [{path}]: {e}')
        sys.exit(1)

    input_file.close()
    return top_ten

###############################################################################
# Code bellow is not considered for your evaluation
###############################################################################

@click.command()
@click.option('--start-date',
              default=(datetime.today() + timedelta(days=-7)).strftime(DATE_FORMAT),
              help='Beginning of the period to consider (inclusive).')
@click.option('--end-date',
              default=datetime.today().strftime(DATE_FORMAT),
              help='End of the period to consider (inclusive).')
@click.argument('input_file_path')
def main_cli(start_date, end_date, input_file_path):
    """
    Entry point for the application. Parses command-line arguments and calls main logic:
    `calculate_totals`. Then prints the results.
    """
    try:
        result = calculate_totals(input_file_path, start_date, end_date)
    except IOError:
        sys.exit(1)
    else:
        result_as_table = tabulate(result, headers=('SKU', 'Revenue (in €)'))
        print(result_as_table)

# For debugging on PyCharm, not really needed.
if __name__ == '__main__':
    main_cli(sys.argv[1:])
