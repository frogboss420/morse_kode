#lister til alfabet og morsekode for at definere key og value
morse=['','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','-.','--','---','.--.','--.-','.-.','...','-','.--','...-','.--','-..-','-.--','--..','.-.-','---.','.--.-','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','.-.-.-','--..--','---...','..--..','-....-','-..-.','....']

alfabet=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å','1','2','3','4','5','6','7','8','9','0','.',',',':','?','-','/','!']

# Dictionary til oversættelse fra bogstaver til morsekode
# Dictionary til oversættelse fra morsekode til bogstaver. Tomt oversættes til mellemrum.
morseCode = {}
morseCodeReverse = {}
for i in range(len(alfabet)):
    morseCode[alfabet[i]]=morse[i]
    morseCodeReverse[morse[i]]=alfabet[i]


# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
def translate(letter, code):
    if str(letter) in code:
        return code[letter]
    else:
        return '?'


# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def encodeMessage(message, code):
    message = str(message)
    out=''
    for i in range (len(message)):
        out+=translate(message[i],code)+'/'
    return out

# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(morseMessage, code):
    separatedMessage = []
    translatedLetters = []
    morseMessage = str(morseMessage)
    separatedMessage = morseMessage.split("/") #Splits the given message at each /, and adds it as a string to the list
    for i in separatedMessage:
        translatedLetters.append(code[i])#adds the translated letters in the translatedLetters list
    translatedMessage = "".join(translatedLetters)#molds the strings together as one. One string to rule them all.
    return translatedMessage

print(decodeMessage('.../---/...//.',morseCodeReverse)) #temporary debugger