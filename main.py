#ghfgj
"""
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total) / len(numbers)
    return total


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    summ = homework * 0.1 + quizzes * 0.3 + tests * 0.6
    return summ


print(get_average(alice))


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(get_letter_grade(get_average(lloyd)))


def get_class_avrg(students):
    students = [lloyd, alice, tyler]
    results = []
    for student in students:
        avrg = get_average(student)
        results.append(avrg)
    return average(results)

"""
"""
minimum = None
maximum = None

while True:
    inp = input('Enter a number: ')
    if inp == 'done': break

    try:
        num = float(inp)
    except:
        print('Invalid input')
        continue

    if minimum is None or num < minimum:
        minimum = num

    if maximum is None or num > maximum:
        maximum = num

print('Maximum:', maximum)
print('Minimum:', minimum)
"""
"""
class MaxSizeList(object):

    def __init__(self):


    def set_list(self, lst):
        self.lst = []

    def get_list(self):
        return self.lst


a = MaxSizeList(3)
b = MaxSizeList(1)


a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")


b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
"""
"""
import abc


class GetSetParent(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super().set_val(value)

    def showdoc(self):
        print("GetSetInt object {}, only accept integer value".format(id(self)))


class GetSetList(GetSetParent):

    def __init__(self, value = 0):
        self.vallist = [value]

    def set_val(self, value):
        self.vallist.append(value)

    def get_val(self):
        return self.vallist[-1]

    def get_vals(self):
        return self.vallist

    def showdoc(self):
        print("GetSetList object, len {}, "
        "stores history of value set".format(len(self.vallist)))


x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()

gsl = GetSetList(5)
gsl.set_val(101)
gsl.set_val(200)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()
"""
"""
import abc
from datetime import datetime

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        fh = open(self.filename, "a")
        fh.write(text + "\n")
        fh.close()

    def read(self):
        readfile = open(self.filename, "w")
        st = readfile.read()
        readfile.close()
        print(st)
class LogFile(WriteFile):

    def write(self, this_line):
        dt = datetime.now()
        date_str = dt.strftime("%Y-%m-%d  %H:%M")
        self.write_line("{0}    {1}".format(date_str, this_line))

class DelimFile(WriteFile):

    def __init__(self, filename, delim):
        super().__init__(filename)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)


log = LogFile("log.txt")
log.write("this is a log message")
#log.read()

csv = DelimFile("text.csv", ",")
csv.write(["1", "2", "3", "4"])
csv.write(["a", "b", "c", "d"])
"""

"""
import abc
import datetime

class WriteFile(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        file = open(self.filename, "a")
        file.write(text + "\n")
        file.close()

    def reado(self):
        readit = open(self.filename, "r+")
        red = readit.read()
        print(red)
        readit.close()

class DelimFile(WriteFile):

    def __init__(self, filename, delim):
        super().__init__(filename)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        return self.write_line(line)

class LogFile(WriteFile):

    def write(self, this_line):
        dt_str = datetime.datetime.now().strftime("%Y-%m-%d\t%H:%M")
        return self.write_line("{0}\t{1}".format(dt_str, this_line))


log = LogFile("log.txt")
log.write("This is a recorded message")

csv = DelimFile("text.csv", ",")
csv.write(["1", "2", "456442", "jbhcfjhdgsh"])
"""
"""
from datetime import datetime


class WriteFile(object):

    def __init__(self, filename, writer):
        self.fh = open(filename, "w")
        self.formatter = writer()

    def write(self, text):
        self.fh.write(self.formatter.format(text))
        self.fh.write("\n")

    def close(self):
        self.fh.close()

class CSVFormatter(object):

    def __init__(self):
        self.delim = ","

    def format(self, this_list):
        new_list = []
        for element in this_list:
            if self.delim in element:
                new_list.append('"{}"'.format(element))
            else:
                new_list.append(element)
        return self.delim.join(new_list)

class LogFormatter(object):

    def format(self, this_line):
        st_str = datetime.now().strftime("%Y-%m-%d  %H:$M")
        return "{0}     {1}".format(st_str, this_line)


writecsv = WriteFile("text2.csv", CSVFormatter)
writelog = WriteFile("log2.txt", LogFormatter)

writecsv.write(["a", "b,2", "c", "d"])
writelog.write("This is a log message")

writecsv.close()
writelog.close()
"""
"""
name = input("Enter File name: ")
handle = open(name, "r")
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
"""
"""
suff = {"s":1, "d":2, "f":5}
for x in suff:
    print(x)
#print(suff.get("candy", -1))
"""
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dico = dict()
count = []
for line in handle:
    line.rstrip()
    if not line.startswith("From "): countinue
    words = line.split()
    count.append(words[1])


for x in count:
    dico[x] = dico.get(x, 0) + 1


bigcount = None
Bigword = None
for w, v in dico.items():
    if bigcount is None or v > bigcount:
        bigword = w
        bigcount = v

print bigword, bigcount
"""
"""
c = {"a": 10, "b": 1, "c": 22}
tmp = []
for k, v in c.items():
    tmp.append((v, k))
print(tmp)
tmp.sort(reverse=False)
print(tmp)
"""
"""
import re
import sys
from PyQt4 import QtGui


h = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
print(re.findall("\S+?@\S+", h))

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

"""

from PyQt4 import QtCore
from PyQt4 import QtGui
import beautiful soap





























