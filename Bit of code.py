ACUTE = "\u0301"
GRAVE = "\u0300"
CIRCUMFLEX = "\u0342"
list(map(chr, range(97, 123)))
#list(map(chr, range(ord('α', ord('ω')))
#list(map(chr, range(ord('a'), ord('z'))))
#print (greeklets)

unicodedata.normalize("NFC", "".join(
    ch
    for ch in unicodedata.normalize("NFD", text)
    #if ch not in [range (ord('A', ord('Z')))]:
    if ch not in [ACUTE, GRAVE, CIRCUMFLEX])
)
