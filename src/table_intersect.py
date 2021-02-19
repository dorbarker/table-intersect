import argparse
import csv
from typing import Set, List
import functools


def arguments():

    desc = """Takes delimited files and writes a copy of each
    containing the intersect of the leftmost column of all the files.
    """.strip()

    epi = "Dillon O.R. Barker (c) 2021"

    parser = argparse.ArgumentParser( description=desc, epilog=epi)

    parser.add_argument('--delimiter', '-d',
                        default='\t',
                        metavar='CHAR',
                        help='Table delimiter; same for all files [TAB]')

    parser.add_argument('inputs', nargs='+',
                        metavar='PATH',
                        help='Input files')

    return parser.parse_args()


def main():

    args = arguments()

    values = intersect_left_columns(args.inputs, args.delimiter)

    write_files(args.inputs, args.delimiter, values)


def left_column(path: str, delimiter: str) -> Set[str]:

    values = set()
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter=delimiter)

        next(reader) # skip the header

        for row in reader:
            values.add(row[0])

    return values


def intersect_left_columns(paths: List[str], delimiter: str) -> Set[str]:

    left_columns = (left_column(p, delimiter) for p in paths)

    return functools.reduce(set.intersection, left_columns)


def write_intersected_file(path: str, delimiter: str, values: Set[str]):

    with open(path, 'r') as i, open(f'{path}.matched', 'w') as o:

        reader = csv.reader(i, delimiter=delimiter)
        writer = csv.writer(o, delimiter=delimiter)

        header = next(reader)

        writer.writerow(header)

        for row in reader:
            if row[0] in values:
                writer.writerow(row)


def write_files(paths: List[str], delimiter: str, values: Set[str]):

    for p in paths:

        write_intersected_file(p, delimiter, values)


if __name__ == '__main__':
    main()

