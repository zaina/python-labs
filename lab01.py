 #!/usr/local/bin/python

import argparse
from random import choice

parser = argparse.ArgumentParser(description='Patent database search engine')
parser.add_argument('--author', metavar='author', type=str, nargs='+',help='author last first')
parser.add_argument('--patent', metavar='patent', type=str, nargs='+',help='patent')
parser.add_argument('--filing_date', metavar='filing_date', type=str, nargs='+',help='filing_date')

args = parser.parse_args()
print args
print args.author

def find_by_author():
    print "find_by_author"

def find_by_patent_number():
    print "find_by_patent_number"

def find_by_filing_date():
    print "find_by_filing"


def test_db_load():
    functions_list = [find_by_filing_date, find_by_patent_number, find_by_author]
    function = choice(functions_list)
    print function
    function()
    return None

test_db_load()
