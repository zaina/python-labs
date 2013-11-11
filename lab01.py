 #!/usr/local/bin/python

"""
:mod:`lab01_pyreview` -- Python review
=========================================

LAB01 Learning Objective: Familiarization with argparse and parsing command line arguments.


a. Review argparse module documentation

b. Build an ArgumentParser object using the following parameters: 
   description: "Patent database search engine"

c. Add support for the following arguments and argument attributes: 
   -a --author last first
   -p --patent_num
   -f --filing_date

d. Run parse_args() to build arguments objects and print the Namespace

e. Construct a generator called test_db_load() that returns a random function from a list of functions.
   The list will support find_by_author(), find_by_patent_number(), and find_by_filing date()
   Test your generator with stub functions
"""

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
