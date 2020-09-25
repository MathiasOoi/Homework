import xml.etree.ElementTree as etree
from collections import defaultdict
import sqlite3
import string
import time
import os


PATH_WIKI_XML = 'D:\\Wikipedia\\'
FILENAME_WIKI = 'enwiki-20200901-pages-articles-multistream.xml'

connection = sqlite3.connect('wiki.db')


def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def strip_tag_name(t):
    for i in range(len(t)-1, 0, -1):
        if t[i] == "}":
            return t[i+1: len(t)]

def parsePage(title, text):
    """
    Iterates over the page ONCE does a few things
    1) Determines the gender by counting pronouns
    2) Parses the info box into dict that maps the title of the page
       to another dict
    3) Counts the amount of words
    4) Will break if the page is not about a person
    :param text: String wiki page
    :return: Tuple of (gender, info box, words)
    """
    def parseInfobox(title, infobox):
        """
        Helper function to help parse infobox
        :param infobox: List of infobox split by \n
        :return: Dict that maps the title of the page to another dict
        """
        d = defaultdict(list)
        lineCounter = 0
        for line in infobox:
            lineCounter += 1
            if line[0] == "|":  # Checks if that line has a new key
                s = line.strip("| ")
                for i in range(len(s)):
                    if s[i] == "=":
                        break
                key = s[:i].strip(" ")
                try:
                    if s[i+2] != "{":
                        for k in range(i, len(s)):
                            if s[k] == "<":  # removes an editor note "<!--- [note]"
                                break
                        # Appends value to a key if that key only has ONE value
                        # I.e. "| children            = 8"
                        d[key].append(s[i+2: k+1])
                except IndexError:
                    continue
                else:
                    if s[i+4: i+9] == "hlist":
                        # Parses out an hlist which is an horizontal list seperated by "|"
                        # i.e. "{{hlist|elem1|elem2|elem3}}"
                        for k in range(i+9, len(s)):
                            if s[k] == "<":
                                break
                        # Split the hlist
                        l = s[i+10: k].split("|")
                        for item in l:  # Append every item in the hlist to the dict
                            d[key].append(item.strip("}").strip("{").strip("[[").strip("]]"))
                    elif s[i+4: i+13] == "flatlist" or s[i+4: i+13] == "plainlist":
                        # Parses out a flatlist and plainlist
                        # https://en.wikipedia.org/wiki/Template:Plainlist
                        # https://en.wikipedia.org/wiki/Template:Flatlist
                        for currlst in range(lineCounter, len(infobox)):
                            if infobox[currlst][:2] == "}}":
                                break
                        lst = infobox[lineCounter: currlst]
                        for item in lst:
                            d[key].append(item.strip("*").strip("{").strip("}").replace("[", "").replace("]", "").replace("end=div", ""))
        return d

    def findInfobox(text):
        """
        Given some wikipedia article return a string of the infobox
        :param text: String
        :return: String
        """
        openCurly = 0
        start, stop = 0, 0
        text = text.split("\n")
        for i in range(len(text)):
            if text[i][2:9] == "Infobox":
                start = i
            if start:
                for char in text[i]:
                    if char == "{":
                        openCurly += 1
                    elif char == "}":
                        openCurly -= 1
                if not openCurly:
                    stop = i
                    break
        return text[start: stop+1]

    def findGenderAndWords(text):
        """
        Counts the male and female pronouns in the text and then returns the gender
        1. Male
        2. Female
        3. Other
        :param text: List
        :return: String
        """
        malePronoun = ["him", "his", "he", "he's"]
        femalePronoun = ["her", "she","she's", "hers"]
        words = len(text)
        maleCount, femaleCount = 0, 0
        for word in text:
            word = word.strip("*").strip("{").strip("}").replace("[", "").replace("]", "")
            if word in malePronoun:
                maleCount += 1
            elif word in femalePronoun:
                femaleCount += 1
        if maleCount > femaleCount:
            return "male", words
        elif femaleCount > maleCount:
            return "female", words
        else:
            return "other", words



    d = parseInfobox(title, findInfobox(text))
    gender, words = findGenderAndWords(text.split())
    print(d)
    print(gender)
    print(words)








pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)

totalCount = 0
articleCount = 0
redirectCount = 0
templateCount = 0
title = None
start_time = time.time()

with open("sample.txt", encoding="utf-8") as fin:
    s = fin.read()
    parsePage("aa", s)

if __name__ == "__main__":
    pass
    for event, elem in etree.iterparse(pathWikiXML, events=('start', 'end')):
        tname = strip_tag_name(elem.tag)
        if event == 'start':
            if tname == 'page':
                title = ''
                id = -1
                redirect = ''
                inrevision = False
                ns = 0
            elif tname == 'revision':
                # Do not pick up on revision id's
                inrevision = True
        else:
            if tname == 'title':
                title = elem.text
                print(title)
            if tname == "text":
                parsePage(title, elem.text)
            elif tname == 'page':
                totalCount += 1
            if totalCount > 0:
                break

            if totalCount > 1 and (totalCount % 100000) == 0:
                print("{:,}".format(totalCount))

            elem.clear()

    elapsed_time = time.time() - start_time

    print("Total pages: {:,}".format(totalCount))
    print("Template pages: {:,}".format(templateCount))
    print("Article pages: {:,}".format(articleCount))
    print("Redirect pages: {:,}".format(redirectCount))
    print("Elapsed time: {}".format(hms_string(elapsed_time)))