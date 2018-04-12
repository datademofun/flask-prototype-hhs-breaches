import csv
from os.path import join
DATA_FILEPATH = join('static', 'data', 'breaches.csv')


def read_spreadsheet():
    """
    Opens the text file at static/data/breaches.csv and parses it

    Returns a Python list of dictionaries
    """
    txtlines = open(DATA_FILEPATH).readlines()
    rows = list(csv.DictReader(txtlines))
    return rows


def find_breaches_by_state(state_abbrev):
    """
    filter the spreadsheet for rows in which state == state_abbrev
    """
    records = read_spreadsheet()
    state_records = []
    for row in records:
        if row['State'] == state_abbrev:
            state_records.append(row)
    return state_records


def find_breach_by_id(id):
    records = read_spreadsheet()
    for row in records:
        if row['id'] == id:
            return row
    ### if function hasn't returned by now, then id is invalid
    abort(404)


