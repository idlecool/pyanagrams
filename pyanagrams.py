import urllib
from BeautifulSoup import BeautifulSoup
webservice = 'http://wordsmith.org/anagram/'
urlprefix = 'anagram.cgi?anagram='
urlsuffix = '&t=1000&a=n'
def getAnagrams(word):
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
