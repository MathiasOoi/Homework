import xml.etree.ElementTree as etree
from collections import defaultdict
import wikitextparser as wtp
import sqlite3
import string
import time
import os

PATH_WIKI_XML = 'D:\\Wikipedia\\'
FILENAME_WIKI = 'enwiki-20200901-pages-articles-multistream.xml'



def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def strip_tag_name(t):
    for i in range(len(t) - 1, 0, -1):
        if t[i] == "}":
            return t[i + 1: len(t)]


def exclude(elem):
    # Skip redirects
    if elem.find('redirect') is not None:
        return True
    # Skip non-article pages.
    # Note that you may need error handling
    if elem.find('ns') is None or elem.find('ns').text != '0':
        return True

    # We don't have any reason to exclude it, so return
    # False (keep it).
    return False


class WikiDB:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS articles (pageid integer, title text);
        """)
        self.conn.commit()
    def insert(self, pageid, title):
        self.conn.execute("""
        INSERT INTO articles VALUES (?, ?);
        """, (pageid, title))
        self.conn.commit()




def parsePage(elem, db):
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
    if not exclude(elem):
        return
    pageid = elem.find("id").text
    title = elem.find('title').text
    article = elem.find('revision/text').text
    db.insert(pageid, title)
    return

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
                i = s.index("=")
                key = s[:i].strip(" ")
                try:
                    if s[i + 2] != "{":
                        for k in range(i, len(s)):
                            if s[k] == "<":  # removes an editor note "<!--- [note]"
                                break
                        # Appends value to a key if that key only has ONE value
                        # I.e. "| children            = 8"
                        d[key].append(s[i + 2: k + 1])
                except IndexError:
                    continue
                else:
                    if s[i + 4: i + 9] == "hlist":
                        # Parses out an hlist which is an horizontal list seperated by "|"
                        # i.e. "{{hlist|elem1|elem2|elem3}}"
                        for k in range(i + 9, len(s)):
                            if s[k] == "<":
                                break
                        # Split the hlist
                        l = s[i + 10: k].split("|")
                        for item in l:  # Append every item in the hlist to the dict
                            d[key].append(item.strip("}").strip("{").strip("[[").strip("]]"))
                    elif s[i + 4: i + 13] == "flatlist" or s[i + 4: i + 13] == "plainlist":
                        # Parses out a flatlist and plainlist
                        # https://en.wikipedia.org/wiki/Template:Plainlist
                        # https://en.wikipedia.org/wiki/Template:Flatlist
                        for currlst in range(lineCounter, len(infobox)):
                            if infobox[currlst][:2] == "}}":
                                break
                        lst = infobox[lineCounter: currlst]
                        for item in lst:
                            d[key].append(
                                item.strip("*").strip("{").strip("}").replace("[", "").replace("]", "").replace(
                                    "end=div", ""))
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
        return text[start: stop + 1]

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
        femalePronoun = ["her", "she", "she's", "hers"]
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

    #d = parseInfobox(title, findInfobox(text))
    #gender, words = findGenderAndWords(text.split())
    #print(d)
    #print(gender)
    #print(words)


pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)

start_time = time.time()

def main(file):
    db = WikiDB("wiki.db")
    for event, elem in etree.iterparse(file, events=('end',)):
        elem.tag = strip_tag_name(elem.tag)
        if elem.tag == "page":
            parsePage(elem, db)
            elem.clear()
            break

    elapsed_time = time.time() - start_time

    print("Elapsed time: {}".format(hms_string(elapsed_time)))


if __name__ == "__main__":
    main(pathWikiXML)
