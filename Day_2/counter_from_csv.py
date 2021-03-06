# -*- coding: utf-8 -*-
"""A module that counts the values in dictionary by keys from a CSV file

This module demonstrates a counter of values in dictionary by keys
based on the list of records which is taken from a CSV file

Example:
    As an input it reads the CSV file that is passed through a command-line
    As an output it sends a list of counters::

        [{'key': 'success', 'value': True, 'count': 476}, {'key': ....

"""

import csv
import argparse
from collections import defaultdict


def name_via_parsing():
    """The function for getting the file's name through parsing

    Returns:
        str: the file's name.

    """
    # creating a parser
    parser = argparse.ArgumentParser(
        description='Process CSV file'
    )
    # adding arguments
    parser.add_argument(
        'input_file',
        metavar='csv file',
        type=str,
        help='an input csv file to read the dictionary'
    )

    args = parser.parse_args()

    return args.input_file


def dict_to_count(file_name):
    """The function that reads records from a file

     Args:
        file_name (str): the file's name.

    Returns:
        list: a list of records.

    """
    # a list that will be containing our records
    records = list()
    with open(file_name) as csvfile:
        # here we tell that we want to open it as a dict
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)
    return records


def list_counter(records):
    """The functions that creates a list of counters

    This function consists of two parts. In the first part we count the same
    values of keys and put them in a result dict and in the second part we
    form our dict to be a list and look according to our expectations

    Args:
        records (list): a list of records read from a CSV file.

    Returns:
        list: a list of counters.

    """
    # this function consists of two parts

    # in this part we count the same values of keys

    # we use defaultdict(dict) as it uses the default value (which is dict,
    # the empty dict) if it encounters an unknown value
    result = defaultdict(dict)
    # for each record
    for each in records:
        # for each key
        for k in records[0].keys():
            try:
                # each[k] - the value of the particular key,
                #  we're about to increment it
                result[k][each[k]] += 1
            except KeyError:
                # or to create it :)
                result[k][each[k]] = 1
    # as a result we'll get sth like {{success: {True: 5000,
    #  False: 5000}}, {{name: {alex: 1, john: 3...

    # creating the final list
    # now we need to meet the requirements of how the counter
    # list should look like
    # let's create an empty list list
    c_list = list()
    for key, v in result.items():
        # e.g. key=success, v = (True: 5000, False: 5000)
        for value in v.items():
            # e.g. value[0] = True, value[1] = 5000
            c_list.append(
                dict(
                    key=key,
                    value=value[0],
                    counter=value[1]
                )
            )
            # so we have sth like {key=success, value=True, counter=5000}
    return c_list


def main():
    # get the name of the input file through parsing ( we must specify
    # the input file in the command line)
    file_name = name_via_parsing()
    # make the list of records that are contained in the input file
    records = dict_to_count(file_name)
    # make a counter list based on the records
    result = list_counter(records)
    print(result)


if __name__ == '__main__':
    main()
