import urllib
from BeautifulSoup import BeautifulSoup
servicedomain = 'http://wordsmith.org'
webservice = 'http://wordsmith.org/anagram/'
urlprefix = 'anagram.cgi?anagram='
urlsuffix = '&t=1000&a=n'

def getAnagrams(word):
    """ Gets anagrams for given word, return value will be a list how to call: getAnagram(str(word)) """
    processurl = webservice+urlprefix+word+urlsuffix
    stream = urllib.urlopen(processurl).read()
    soup = BeautifulSoup(stream)
    body = soup.contents[2]
    block = body.contents[3]
    list = block.contents[5]
    words = list.contents[7]
    wordstring = words.prettify()
    wordlist = wordstring.split('\n<br />\n')[1:-1]
    return wordlist

def getGif(sourceString,targetString,textColor='#00FFFF',backgroundColor='#FF0000',border_color='#000000',delay='slow'):
    """ Gets the GIF animation for provided anagram, return value will be a binary stream, how to call: getGif(sourceString,targetString[,textColor][,backgroundColor][,border_color][,delay]) all colour should be RGB Hex coded ex: #FF09E7 and delay has three options ['fast','medium','slow']"""
    # anagram check fot source and target strings
    sourceString=sourceString.lower()
    targetString=targetString.lower()
    sName = list(sourceString)
    tName = list(targetString)
    for i in xrange(sName.count(' ')):
        sName.remove(' ')
    for i in xrange(tName.count(' ')):
        tName.remove(' ')
    if(len(sName) != len(tName)):
        raise AnagramException(sourceString, targetString)
    for char in sName:
        try:
            tName.remove(char)
        except:
            raise AnagramException(sName, tName)
    
    #prepare url to generate gif
    gifcgi = 'animation.cgi?'
    processurl=webservice+gifcgi+urllib.urlencode({'sourceString':sourceString, 'submit':'Generate Animated Gif', 'targetString':targetString, 'textColor':textColor, 'backgroundColor':backgroundColor, 'border_color':border_color, 'delay':delay })
    stream = urllib.urlopen(processurl).read()
    soup = BeautifulSoup(stream)
    body = soup.contents[2]
    cont = body.contents[3]
    cont2 = cont.contents[5]
    cont3 = cont2.contents[7]
    imgelement = str(cont3.extract())
    urlpath = imgelement.split('"')[1]
    imgurl = servicedomain + urlpath
    
    #fetch the gif image
    stream = urllib.urlopen(imgurl).read()
    return stream

class AnagramException(Exception):
    def __init__(self, sName, tName):
        self.sName = sName
        self.tName = tName
    def __str__(self):
        return "'"+self.sName+"' & '"+self.tName+"' are not anagrams!!!"
