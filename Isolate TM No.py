# This program takes the list of output from an LDAB search and isolates the TM numbers

from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
inputfile = askopenfilename(defaultextension='.txt', title='Input File') # show an "Open" dialog box and return the path to the selected file
if inputfile == '':  # asksaveasfile return `None` if dialog closed with "cancel".
    exit()
# print (filename)
# from tkinter.filedialog import asksaveasfilename
# outputfile = asksaveasfilename(defaultextension=".txt", title="Save As") # show a "Save as" dialog box and return the path to the selected file
# if outputfile == '': # asksaveasfile return `None` if dialog closed with "cancel".
#     sys.exit()
#
# outfile = open(outputfile, 'w+')   #open output file and create a new one if needed
#
# import unicodedata2


newline: str = ''
line = ''
i: int = 0


with open(inputfile) as infile:
    for line in infile:
        # print (line)
        result = line[3:-1].find(" ")
        result +=3
        newline = line[3:result]
        print (newline)


