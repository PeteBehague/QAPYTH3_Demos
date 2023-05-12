import csv
import pprint

with open('passwd', 'rt') as csvfile:
     pwreader = csv.reader(csvfile, delimiter=':')
     for row in pwreader:
        print(', '.join(row))

fields = ['user', 'pw'  'uid', 'gid', 'txt', 'home', 'shell']
with open('passwd', 'rt') as csvfile:
    dtreader = csv.DictReader(csvfile,
        fieldnames=fields,
        delimiter=':')
    for dtline in dtreader:
        pprint.pprint(dtline)
