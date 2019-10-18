import csv

from pathlib import Path

def parse_from_csv(csv_path, outfile, fieldname=None, delimiter=','):

    if not fieldname:
        raise ValueError('The CSV fieldname for text content cannot be None')

    in_csv = Path(csv_path)

    with open(outfile, 'w') as f_out:
        with open(in_csv, mode='r') as f_in:

            reader = csv.DictReader(f_in)

            for row in reader:
                f_out.write(row[fieldname] + '\n')
