# This program takes the unicode output from the Ibycus program Takitouni and converts to unicode
# for transferring files from Ibycus that have Greek

from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
inputfile = askopenfilename(defaultextension='.txt', title='Hex File') # show an "Open" dialog box and return the path to the selected file
if inputfile == '':  # asksaveasfile return `None` if dialog closed with "cancel".
    exit()
# print (filename)
from tkinter.filedialog import asksaveasfilename
outputfile = asksaveasfilename(defaultextension=".txt", title="Save As") # show a "Save as" dialog box and return the path to the selected file
if outputfile == '': # asksaveasfile return `None` if dialog closed with "cancel".
    sys.exit()

outfile = open(outputfile, 'w+')   #open output file and create a new one if needed

import unicodedata2


newline = ''
line = ''
i = 0


with open(inputfile) as infile:
    for line in infile:
        # print (line)
        x = len(line)
        # print (x)
        while i < len(line):
            unicharcode = line[i:(i+4)]
            # print (unicharcode)
            if unicharcode == '000a':
                newline = unicodedata2.normalize("NFC", newline) + '\n'
                outfile.write(newline)
                # print(newline)
                newline = ''
            else:
                newline = newline + chr(int(unicharcode, 16))
            i += 4
            # print (i)

