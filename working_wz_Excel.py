import xlrd
import xlwt
import pprint


datafile = "tamplate.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
             for col in range(sheet.ncols)]
                for r in range(sheet.nrows)]

    print("\nList Comprehension")
    print("data[3][2]:"),
    print(data[3][2])

    print("\nCells in a nested loop:")
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50
                print(sheet.cell_value(row, col)),


    ###other useful methods:
    print("\nRows, Columns, and Cells:")
    print("Number of rows in the sheet:"),
    print(sheet.nrows)
    print("Types of data in cell (row 3, col 2):"),
    print(sheet.cell_type(3, 2))
    print("Value in cell (row 3, col 2):"),
    print(sheet.cell_value(3, 2))
    print("Get a slice of values in column 3, from row 1-3:")
    print(sheet.col_values(3, start_rowx=1, end_rowx=4))

    print("\nDates:")
    print("Type of data in cell (row 1, col 0):")
    print(sheet.cell_type(1, 0))
    exceltime = sheet.cell_value(1, 0)
    print("Time in Excel format:"),
    print(exceltime)
    print("Convert time to a Python datetime tuple, from the Excel float:"),
    print(xlrd.xldate_as_tuple(exceltime, 0))

    data = {
        'maxtime': (0, 0, 0, 0, 0, 0),
        'maxvlue': 0,
        'mintime': (0, 0, 0, 0, 0, 0),
        'minvalue': 0,
        'avgcoast': 0
    }
    return data


    data = parse_file(datafile)

###################################################################################

datafile = "template.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)]
                for r in range(sheet.nrows)]

    cv = sheet.col_values(1, startrowx=1, endrowx=None)

    maxval = max(cv)
    minval= min(cv)

    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1

    maxtime = sheet.cell_value(maxpos, 0)
    realtime = xlrd.xldate_as_tuple(maxtime, 0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)

    data = {
        'maxtime': realtime,
        'maxvalue': maxval,
        'mintime': realmintime,
        'minvalue': minval,
        'avgcoast': sum(cv) / float(len(cv))
    }

    return data

data = parse_file(datafile)
pprint.pprint(data)


assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
assert round(data['maxvalue'], 10 ) == round(18779.02551, 10)
