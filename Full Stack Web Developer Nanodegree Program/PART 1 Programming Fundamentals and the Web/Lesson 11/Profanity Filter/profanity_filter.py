import urllib
def read_text():
    quotes = open("C:\Python27\Udacity Projects\Profanity Filter\movie_quotes.txt")
    contentsOfFile = quotes.read()
    quotes.close()
    
    #print (contentsOfFile)
    check_profanity(contentsOfFile)

def check_profanity(textToCheck):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+textToCheck)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!!")
    else:
        print("Cannot read text!!")
    
read_text()

