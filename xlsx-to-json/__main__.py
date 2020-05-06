from .converter import Converter
from argparse import RawTextHelpFormatter
import argparse

def main():
    parser = argparse.ArgumentParser(description = '''
    Convert .xlsx files to json
    foo.bar.field3 should be represented in the excel sheet as the column foo__bar__field3
    The value stored in this column will be used as the value for that field

    Each row is treated as a single json object.
    Multiple rows in the sheet generate an array of these json objects.    
    Empty cells are neglected.
    ''', formatter_class=RawTextHelpFormatter)
    parser.add_argument('xlsx_path', help = 'Path to excel sheet')
    parser.add_argument('out_path', help = 'Path to output file. JSON extension needs to be specified in file name')

    args = parser.parse_args()
    with open(args.out_path, 'w') as f:
        converter = Converter(f)
        converter.convert(args.xlsx_path)

if __name__ == '__main__':
    main()