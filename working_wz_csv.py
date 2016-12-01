import csv
import os
import pprint



DATADIR = r"C:\Users\Muhammad\PycharmProjects\testing"
DATAFILE = "DriverDesp.csv"

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile, "r") as sd:
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
        return data

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    parse_csv(datafile)
    d = parse_csv(datafile)
    pprint.pprint(d)