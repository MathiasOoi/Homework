import xml.etree.ElementTree as etree
from collections import defaultdict
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
        :param infobox: String
        :return: Dict that maps the title of the page to another dict
        """
        d = defaultdict(list)
        infobox = infobox.split("\n")
        lineCounter = 0
        for line in infobox:
            lineCounter += 1
            if line[0] == "|":  # Checks if that line has a new key
                s = line.strip("| ")
                for i in range(len(s)):
                    if s[i] == "=":
                        break
                key = s[:i].strip(" ")
                if s[i+2] != "{":
                    for k in range(i, len(s)):
                        if s[k] == "<":
                            break
                    d[key].append(s[i+2: k+1])
                else:
                    if s[i+4: i+9] == "hlist":
                        for k in range(i+9, len(s)):
                            if s[k] == "<":
                                break
                        l = s[i+10: k].split("|")
                        for item in l:
                            d[key].append(item.strip("}").strip("{").strip("[[").strip("]]"))
                    elif s[i+4: i+13] == "plainlist":
                        print(line)
                        for currPlainlist in range(lineCounter, len(infobox)):
                            if infobox[currPlainlist][:2] == "}}":
                                break
                        plainlist = infobox[lineCounter: currPlainlist]

                    else:
                        pass


        print(d)

    parseInfobox(title, """{{Infobox person ii
| honorific_suffix    = {{post-nominals|CBE}}
| image               = David Gilmour Argentina 2015 (cropped).jpg<!-- NOTE: Do not replace David Gilmour Argentina 2015 (cropped).jpg without consensus on the talk page -->
| alt                 = Gilmour playing onstage
| caption             = Gilmour performing in 2015
| birth_name          = David Jon Gilmour
| birth_date          = {{Birth date and age|1946|03|06|df=y}}
| birth_place         = [[Cambridge]], England
| occupation          = {{hlist|Singer|songwriter|musician}}<!--Please do not add to this list without first discussing your proposal on the talk page. -->
| spouse              = {{plainlist|
*{{marriage|[[Ginger Gilmour|Virginia "Ginger" Hasenbein]]|1975|1990|end=div}}
*{{marriage|[[Polly Samson]]|1994}}
}}
| years_active        = 1963–present
| children            = 8
| website             = {{URL|davidgilmour.com}}
| module              = {{Infobox musical artist|embed=yes
| background          = solo_singer
| genre               = {{hlist|[[Progressive rock]]|[[psychedelic rock]]|[[art rock]]|[[Ambient music|ambient]]|[[blues rock]]}}
| instrument          = {{hlist|Guitar|vocals}}<!--- If you think an instrument should be listed or removed, a discussion to reach consensus is needed first per: https://en.wikipedia.org/wiki/Template:Infobox_musical_artist#instrument--->
| label               = {{hlist|[[Columbia Graphophone Company|EMI Columbia]]|[[Harvest Records|Harvest]]|[[Capitol Records|Capitol]]|[[Columbia Records|Columbia]]|[[Sony Music Entertainment|Sony]]|[[EMI]]}}
| associated_acts     = {{hlist|[[Pink Floyd]]|[[Jokers Wild (band)|Jokers Wild]]|[[Syd Barrett]]|[[Kate Bush]]|[[The Strat Pack]]|[[the Orb]]|[[Paul McCartney]]|[[Roy Harper (singer)|Roy Harper]]}}<!--Please do not add to this list without first discussing your proposal on the talk page. -->
}}}}""")




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

if False:
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
            if tname == "text":
                pass
            if tname == 'title':
                title = elem.text
            elif tname == 'page':
                totalCount += 1
            if totalCount > 1:
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