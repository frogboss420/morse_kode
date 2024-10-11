#Lister til alfabet og morsekode for at definere key og value
morse=['','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.-.-','---.','.--.-','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----','.-.-.-','--..--','---...','-.-.-.','..--..','-....-','-..-.','-.-.--']
alfabet=[' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å','1','2','3','4','5','6','7','8','9','0','.',',',':',';','?','-','/','!']

morseCode = {} # Dictionary til oversættelse fra bogstaver til morsekode
morseCodeReverse = {} # Dictionary til oversættelse fra morsekode til bogstaver. Tomt oversættes til mellemrum.
for i in range(len(alfabet)):
    morseCode[alfabet[i]]=morse[i]
    morseCodeReverse[morse[i]]=alfabet[i]


# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionary (code) hvis muligt, ellers returnerer den et '?'
def translate(letter, code):
    letter = letter.upper()
    if str(letter) in code:
        return code[letter]
    else:
        return '?'


# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def encodeMessage(message, code):
    #Sikrer at den vilkårlige besked er en streng og at alle bogstaver er store bogstaver.
    message = str(message)
    message=message.upper()
    out=''
    #Oversætter alle gyldige tegn i beskeden og tilføjer et '/' ved enden for at separere tegnene.
    for i in range (len(message)):
        out+=translate(message[i],code)+'/'
    #Tjekker om det næstsidste tegn er et '/', så beskeden ender på '//'. Hvis det ikke er tilfældet, tilføjer den det sidste '/' her.
    if out[len(out)-2] != '/':
        out = out.split()
        out.append('/')
        out = ''.join(out)
    return out


# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(morseMessage, code):
    separatedMessage = []
    translatedLetters = []
    morseMessage = str(morseMessage)
    separatedMessage = morseMessage.split("/") #Opdeler den givne besked ved '/', og tilføjer den som en streng til listen
    for i in separatedMessage:
        translatedLetters.append(code[i])
        #Tilføjer oversatte bogstaver til listen translatedLetters
    translatedMessage = "".join(translatedLetters)#Sammenkobler strengene sammen til én.
    return translatedMessage

#Fejlfindingskode.
encoded = encodeMessage('hello my name is JEFF HELLO MY NAME IS jeff g',morseCode)
print(decodeMessage(encoded, morseCodeReverse))
print(encoded)
