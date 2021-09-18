# This program will strip all but the bare greek letters, and deliver a count of max and min letters/line with the average,
# along with letter and line counts for the pages and columns
# Assumes that the file uses:
# ~np for a new page (~np202 for a page that is numbered)
# ~nc for a new column
# | to signal a comment
# The program also gives extant line results for crosschecking
# v 1.0 8-31-21

# Setup unicodedata package and define the greek letters as a list
import unicodedata2

greeklets: str = 'αβγδεζηθικλμνξοπρστυφχψωςϲΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩϹ'
greekletslist = list(greeklets)

#initialize
pagnum = 0
colnum = 1

#initialize for new column/page subroutine

def clear():
    global minlets
    global maxlets
    global totalletters
    global totallines
    global extantminlets
    global extantmaxlets
    global extanttotalletters
    global extanttotallines
    minlets = 10000     #impossibly high letters/line count
    maxlets = 0
    totalletters = 0
    totallines = 0
    extantminlets = 10000
    extantmaxlets = 0
    extanttotalletters = 0
    extanttotallines = 0
    return

#output results subroutine

def printresults():
    results = ('Page ' + str(pagnum) + ', Column ' + str(colnum) + ':')
    results += (' | Letters/line: Min=' + str(minlets) + ', Max=' + str(maxlets) + ', Average=' + str(round((totalletters / totallines), 2)))
    results += (' | Totals/column: ' + str(totalletters) + ' letters, ' + str(totallines) + ' lines')
    print(results)
    results = ('Extant Letters/line: Min=' + str(extantminlets) + ', Max=' + str(extantmaxlets) + ', Average='
    + str(round((extanttotalletters / extanttotallines), 2)) + ', Lines=' + str(extanttotallines))
    print(results)
    return

# File open dialogue function

from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print (filename)

#intialize counters and flag
clear()

# Load line by line

with open(filename, encoding='utf-8') as f:
    for line in f:

        # print(line)

# Check for separator symbol: ~np = new page, ~nc = new column (if followed by digits, that's the real page #)
        tilda = line.find('~')
        if tilda == 0:
            if minlets != 10000:
                #Print results for last page/column unless initialization flag is up
                printresults()
                clear()
            if len(line) >= 2 and line[2] == 'p':
                pagnum += 1
                colnum = 1
                if len(line) > 3 and line[3].isdigit() == True:
                    pagnum = int(line[3:])
            elif len(line) >= 2 and line[2] == 'c':
                colnum += 1
                if len(line) > 3 and line[3].isdigit() == True:
                    colnum = int(line[3:])
            else:
                print('TILDA SYNTAX ERROR')

        # delete everything following the upright vertical, character '|' [=comments]
        vertical = line.find('|')
        line = line[0:vertical].rstrip()
        rbracket = line.find(']')
        if rbracket == (len(line) - 1):
            extant = 0
        else:
            extant = 1

        # use decompose feature in normalize function to strip all unicode characters not in the list
        bareline: str = unicodedata2.normalize("NFC", "".join(
                ch
                for ch in unicodedata2.normalize("NFD", line)

                  if (ch in greekletslist)

            ))

        #print(bareline)

        # maintain counts for min, max and totals
        x = len(bareline)
        if x > 0:
           # print (x)
            totalletters += x
            totallines += 1
            if minlets > x:
                minlets = x
            if maxlets < x:
                maxlets = x
            if extant == 1:
               extanttotalletters += x
               extanttotallines += 1
            if extant == 1 and extantminlets > x:
                extantminlets = x
            if extant == 1 and extantmaxlets < x:
                extantmaxlets = x

#Print results for final page/column
printresults()

