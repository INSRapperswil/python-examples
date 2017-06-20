import json
import csv


def jsonstring2dict(string):
    return json.loads(string)


def jsonfile2dict(filename):
    with open(filename) as fin:
        return json.load(fin)


def csv2dict(filename):
    with open(filename) as fin:
        reader = csv.DictReader(fin)
        return reader

