# -*- coding: utf-8 -*-
__author__ = 'Patric Wust'
# Package 
# Version

import os, re


price_data_dir=os.path.join(os.path.abspath(os.path.curdir),
                            '..', 'old-moc-data', 'umsatz')

products_filename=os.path.join(price_data_dir, 'product.ini')
ausnahme_filename=os.path.join(price_data_dir, 'ausnahme.ini')

all_lines_count = 0
good_lines_count = 0
price_lines_count = 0
name_lines_count = 0
label_lines_count = 0
double_lines_count = 0
current_row = 1
max_rows = 220

product_prices = {}
product_names = {}
product_labels = {}

with open(products_filename, 'r') as prod_file:
    for line in prod_file:
        line = line.rstrip("\r\n\t ")
        all_lines_count += 1
        #if not (line[:1] == '@' or re.match('^\s*$',line)):
        if not (re.match('^(\s*|\s*@+.*)$',line)):
            # search empty lines as well
            good_lines_count += 1
            #print(line)
            if line.split(',')[0] == 'PREIS':
                if line.split(',')[1] in product_prices:
                    print()
                    print('Key %s already stored! (existing: %s, not-stored: %s)' %
                          (line.split(',')[1],product_prices[line.split(',')[1]],line.split(',')[2]))
                    double_lines_count += 1
                else:
                    product_prices[line.split(',')[1]] = line.split(',')[2]
                    price_lines_count += 1
                print('p', end='')
                current_row += 1
                if current_row > max_rows:
                    print()
                    current_row = 1
            elif line.split(',')[0] == 'DEF':
                product_names[line.split(',')[1]] = line.split(',')[2]
                name_lines_count += 1
                print('d', end='')
                current_row += 1
                if current_row > max_rows:
                    print()
                    current_row = 1
            elif line.split(',')[0] == 'LABEL':
                product_labels[line.split(',')[1]] = line.split(',',2)[2]
                label_lines_count += 1
                print('l', end='')
                current_row += 1
                if current_row > max_rows:
                    print()
                    current_row = 1

print()
print('Number of lines: %s (%s good ones, %s prices, %s groups, %s labels, %s double).' %
      (all_lines_count, good_lines_count, price_lines_count, name_lines_count, label_lines_count, double_lines_count))
print('Object lengths: %s prices, %s groups, %s labels.' % (len(product_prices), len(product_names), len(product_labels)))
#print('Label keys: ', product_labels.keys())