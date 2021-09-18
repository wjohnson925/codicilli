# This little program takes in a file with text loaded from TLG,
# divides at each  oblique (/), and formats as a diplomatic transcript
# v 1.0 8-31-21
# Added reset to line numbering when a double oblique (//) is detected
# v1.1 9-18-21

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from easygui import multchoicebox

# Get options

options = ["", "     Insert Iota Adscript", "     Abbreviate Nomina Sacra", "     Keep lines as they are (for poetry)"]
optionschoice = multchoicebox("Select one or more options", "Options", options)

#print(optionschoice)

# Define the table of replacements.
# Define the Greek Unicode alphabet and what we will replace it with. Sigma is special, since we will convert
# to lunate sigma. / is special since that is the signal to split a line. Hyphen is special, since that is the
# signal to join lines
greek_inn: str = ("- / σ Σ α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ τ υ φ χ ψ ω ς "
                + "Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Τ Υ Φ Χ Ψ Ω . · · ; ,   ")
greek_out: str = ("- / ϲ Ϲ α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ τ υ φ χ ψ ω ϲ "
                + "Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Τ Υ Φ Χ Ψ Ω . · · ; ,   ")
# Now define the diacritics tables, to set up stripping accents and breathings
greek_inn = greek_inn + 'ά ἀ ἁ ἂ ἃ ἄ ἅ ἆ ἇ ὰ ά ᾰ ᾱ ᾶ '
greek_out = greek_out + 'α α α α α α α α α α α α α α '
greek_inn = greek_inn + 'Ά Ἀ Ἁ Ἂ Ἃ Ἄ Ἅ Ἆ Ἇ Ὰ Ά Ᾰ Ᾱ '
greek_out = greek_out + 'Α Α Α Α Α Α Α Α Α Α Α Α Α '
greek_inn = greek_inn + 'έ ἐ ἑ ἒ ἓ ἔ ἕ ὲ '
greek_out = greek_out + 'ε ε ε ε ε ε ε ε '
greek_inn = greek_inn + 'Έ Ἐ Ἑ Ἒ Ἓ Ἔ Ἕ Ὲ Έ '
greek_out = greek_out + 'Ε Ε Ε Ε Ε Ε Ε Ε Ε '
greek_inn = greek_inn + 'ή ἠ ἡ ἢ ἣ ἤ ἥ ἦ ἧ ὴ ή ῆ '
greek_out = greek_out + 'η η η η η η η η η η η η '
greek_inn = greek_inn + 'Ή Ἠ Ἡ Ἢ Ἣ Ἤ Ἥ Ἦ Ἧ Ὴ Ή '
greek_out = greek_out + 'Η Η Η Η Η Η Η Η Η Η Η '
greek_inn = greek_inn + 'ἰ ἱ ἲ ἳ ἴ ἵ ἶ ἷ ὶ ί ῐ ῑ ϊ ῒ ΐ ῖ ῗ '
greek_out = greek_out + 'ι ι ι ι ι ι ι ι ι ι ι ι ι ι ι ι ι '
greek_inn = greek_inn + 'Ί Ϊ Ἰ Ἱ Ἳ Ἴ Ἵ Ἶ Ἷ Ῐ Ῑ Ὶ Ί '
greek_out = greek_out + 'Ι Ι Ι Ι Ι Ι Ι Ι Ι Ι Ι Ι Ι '
greek_inn = greek_inn + 'ό ὀ ὁ ὂ ὃ ὄ ὅ ὸ ό '
greek_out = greek_out + 'ο ο ο ο ο ο ο ο ο '
greek_inn = greek_inn + 'Ό Ὀ Ὁ Ὂ Ὃ Ὄ Ὅ Ὸ Ό '
greek_out = greek_out + 'Ο Ο Ο Ο Ο Ο Ο Ο Ο '
greek_inn = greek_inn + 'ὐ ὑ ὒ ὓ ὔ ὕ ὖ ὗ ύ ὺ ῠ ῡ ϋ ῢ ΰ ῦ ῧ '
greek_out = greek_out + 'υ υ υ υ υ υ υ υ υ υ υ υ υ υ υ υ υ '
greek_inn = greek_inn + 'Ύ Ϋ Ὑ Ὓ Ὕ Ὗ Ῠ Ῡ Ὺ Ύ '
greek_out = greek_out + 'Υ Υ Υ Υ Υ Υ Υ Υ Υ Υ '
greek_inn = greek_inn + 'ώ ὠ ὡ ὢ ὣ ὤ ὥ ὦ ὧ ὼ ώ ῶ '
greek_out = greek_out + 'ω ω ω ω ω ω ω ω ω ω ω ω '
greek_inn = greek_inn + 'Ώ Ὠ Ὡ Ὢ Ὣ Ὤ Ὥ Ὦ Ὧ Ὼ Ώ '
greek_out = greek_out + 'Ω Ω Ω Ω Ω Ω Ω Ω Ω Ω Ω '

#Optional definitions depending on Iota Adscript choice
if options[1] in optionschoice:
    print('here')
    greek_inn = greek_inn + 'ᾀ ᾁ ᾂ ᾃ ᾄ ᾅ ᾆ ᾇ ᾲ ᾳ ᾴ ᾷ '
    greek_out = greek_out + 'αιαιαιαιαιαιαιαιαιαιαιαι'
    greek_inn = greek_inn + 'ᾈ ᾉ ᾊ ᾋ ᾌ ᾍ ᾎ ᾏ '
    greek_out = greek_out + 'ΑΙΑΙΑΙΑΙΑΙΑΙΑΙΑΙ'
    greek_inn = greek_inn + 'ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ῂ ῃ ῄ ῇ '
    greek_out = greek_out + 'ηιηιηιηιηιηιηιηιηιηιηιηι'
    greek_inn = greek_inn + 'ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ '
    greek_out = greek_out + 'ΗΙΗΙΗΙΗΙΗΙΗΙΗΙΗΙ'
    greek_inn = greek_inn + 'ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ῲ ῳ ῴ ῷ '
    greek_out = greek_out + 'ωιωιωιωιωιωιωιωιωιωιωιωι'
    greek_inn = greek_inn + 'ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ '
    greek_out = greek_out + 'ΩΙΩΙΩΙΩΙΩΙΩΙΩΙΩΙ'
else:
    greek_inn = greek_inn + 'ᾀ ᾁ ᾂ ᾃ ᾄ ᾅ ᾆ ᾇ ᾲ ᾳ ᾴ ᾷ '
    greek_out = greek_out + 'ᾳ ᾳ ᾳ ᾳ ᾳ ᾳ ᾳ ᾳ ᾳ ᾳ ᾳ ᾳ '
    greek_inn = greek_inn + 'ᾈ ᾉ ᾊ ᾋ ᾌ ᾍ ᾎ ᾏ '
    greek_out = greek_out + 'ᾼ ᾼ ᾼ ᾼ ᾼ ᾼ ᾼ ᾼ '
    greek_inn = greek_inn + 'ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ῂ ῃ ῄ ῇ '
    greek_out = greek_out + 'ῃ ῃ ῃ ῃ ῃ ῃ ῃ ῃ ῃ ῃ ῃ ῃ '
    greek_inn = greek_inn + 'ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ '
    greek_out = greek_out + 'ῌ ῌ ῌ ῌ ῌ ῌ ῌ ῌ '
    greek_inn = greek_inn + 'ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ῲ ῳ ῴ ῷ '
    greek_out = greek_out + 'ῳ ῳ ῳ ῳ ῳ ῳ ῳ ῳ ῳ ῳ ῳ ῳ '
    greek_inn = greek_inn + 'ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ '
    greek_out = greek_out + 'ῼ ῼ ῼ ῼ ῼ ῼ ῼ ῼ '

#Table in case nomina sacra choice is selected
nomsaclist = ['κυριε', 'κε', 'Ιηϲουϲ', 'ιϲ']

# File open dialogue function

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
print (filename)

# Get the file name and load line by line

greektext = ""
with open (filename) as f:
    # greektext = f.read()      # we cannot do this since we need to adjust word breaks at line end, as follows
    for line in f:
        greektext = greektext + line.rstrip()
        if line != "" and line[-1] not in [' ','-']:
            greektext = greektext + ' '     #adjust word break at line end as needed
        #Poetry option
        if options[3] in optionschoice:
            greektext = greektext + '/'  # force break at line end for poetry

        # print (greektext)

# input a line of greek text taken from TLG and with line separation marked by /
i= 0
linenumber = 1
spaceflag = 0
hyphenflag = 0
newtext = ''
newtext = newtext + f'{linenumber:3d}' + '  '
targetletter = ''

while i < len(greektext):
    targetletter: str = greektext[i]
    i += 1
    result:int = greek_inn.find(targetletter)
    if result != -1:

        # Check for symbols needing special treatment
        # Oblique means split the line; hyphen means join and delete space; no duplicate spaces;
        # double oblique means new column/page
        if targetletter in ['/', '-', ' ']:

            if targetletter == '/':
                linenumber = linenumber + 1

                if newtext[-1] not in [' ', '.', '·', ';', ',']:                #if a letter, then need to add a hyphen
                    newtext = newtext + '-'

                if i < len(greektext) and greektext[i]  == '/':                 #reset line count for double oblique
                    linenumber = 1
                    i += 1
                    # print('here')

                newtext = newtext + '  |' + '\n' + f'{linenumber:3d}' + '  '    #add line break and line number
                hyphenflag = 0


            elif targetletter == "-":
               hyphenflag = 1   #to stop non-letter accretion after hyphen

            elif targetletter == " ":
                if spaceflag == 0:
                    if hyphenflag == 0:
                        newtext: str = newtext + " "

                    spaceflag = 1   #to prevent duplicate spaces

        else:
            #     Accumulate the output string, replacing sigmas with lunates
            #resultend = result + 2
            #xxx = greek_out[result:resultend].rstrip()
            #print(targetletter + ' ' + str(result) + ' ' + xxx)
            newtext: str = newtext + greek_out[result:(result + 2)].rstrip()
            spaceflag = 0
            hyphenflag = 0


newtext = newtext + '  |'

#Make substitutions for nomina sacra, if that option is selected
if options[2] in optionschoice:
    for i in range(0, (len(nomsaclist)-1), 2):
        newertext = newtext.replace(nomsaclist[i], nomsaclist[i+1])
        newtext = newertext

print (newtext)
