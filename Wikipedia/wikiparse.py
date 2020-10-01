import xml.etree.ElementTree as etree
from collections import defaultdict
import wikitextparser as wtp
import os, re, sys, time, string, signal, sqlite3

# Useful links
# https://en.wikipedia.org/wiki/Wikipedia:List_of_infoboxes#Arts_and_culture

PATH_WIKI_XML = 'D:\\Wikipedia\\'
FILENAME_WIKI = 'enwiki-20200901-pages-articles-multistream.xml'



def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def strip_tag_name(t):
    return t[t.rfind("}") + 1: len(t)]


def exclude(elem):
    # Skip redirects
    if elem.find('redirect') is not None:
        return True
    # Skip non-article pages.
    # Note that you may need error handling
    if elem.find('ns') is None or elem.find('ns').text != '0':
        return True

    # Skip articles with no text
    if elem.find('revision/text').text is None:
        return True

    # We don't have any reason to exclude it, so return
    # False (keep it).
    return False

def containsSpecialTitle(title, *args):
    for i in args:
        if title.startswith(i):
            return True
    return False


class WikiDB:
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS articles (pageid integer, title text, chars integer);
        """)
        # Spouses is 0 or 1, boolean values
        self.conn.commit()
    def insert(self, pageid, title, chars):
        self.conn.execute("""
        INSERT INTO articles VALUES (?, ?, ?);
        """, (pageid, title, chars))
        self.conn.commit()




def parsePage(elem, db=None):
    """
    :param elem:
    :param db:
    :return:
    """
    if not exclude(elem):
        return

    pageid = elem.find("id").text
    title = elem.find('title').text
    article = elem.find('revision/text').text
    if article is None:
        return
    if article.lower().startswith("#redirect"):
        return
    if article:
        chars = len(article)
    else:
        return

    page = wtp.parse(article)

    # 3 Steps
    # 1) Get the infobox
    # 2) Remove the first and last lines by slicing
    # 3) Turn it into a Table
    # Note: Code skips articles without infoboxes
    infobox = getTemplate(page, "Infobox")
    if inCategories(page, "births"):
        print(title)
        db.insert(pageid, title, chars)
        if infobox is None:
            return
        infobox = infobox[infobox.find("\n") + 1: infobox.rfind("\n")]
        if infobox.count("\n") == 0:  # One line infobox creates an infinite loop
            return
        infobox = wtp.Table(infobox)


        # Iterate over every cell and parse it
        d = defaultdict(list)
        for a in range(len(infobox.cells())):
            for b in range(len(infobox.cells(row=a))):
                parsed = parseCell(str(infobox.cells(row=a, column=b)))
                d[parsed[0]] = parsed[1]
        #db.insert(pageid, title, chars)


def getTemplate(page, template):
    """
    Given a parsed article return the string of given template
    :param page: 'wikitextparser._wikitext.WikiText'
    :param template: String (first part of a template)
    :return: String of Template
    """
    for tm in page.templates:
        tm = str(tm)
        if tm.split("\n")[0].strip("{").startswith(template):
            return tm

def getCategories(page):
    page = str(page).split("\n")
    categories = [line for line in page if line.startswith("[[Category:")]
    if categories:
        print(categories)
    return categories

def inCategories(page, value):
    for c in getCategories(page):
        if value in c:
            return True
    return False


def getGender(page):
    pass

def removeNotes(s):
    """
    text <--! note
    Remove everything past the <!--
    """
    try:
        return s[:s.index("<!--")]
    except ValueError:
        return s

def parseCell(cell):
    """
    :param cell: String (Wikipedia infobox cell)
    :return: Tuple (String, List)
    """
    cell = cell.strip("\n| ")
    key, value = cell[:cell.find("=")].strip(" "), cell[cell.find("=")+2:]
    value = removeNotes(value)
    if value.startswith("{{"):
        value = value.strip("{{").strip("}}")
        if value.startswith("hlist"):
            value = value.strip("hlist").split("|")
            return key, value[1:]
        elif value.startswith("plainlist"):
            value = value.split("\n")[1:-1]
            return key, [v.strip("*{{").strip("}}") for v in value]
        else:
            return key, [value]

    else:
        return key, [value]






pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)
start_time = time.time()


def main(file):
    db = WikiDB("wiki.db")
    db.insert(0, "Test", 0)
    pageCount = 0
    for event, elem in etree.iterparse(file, events=('end',)):
        elem.tag = strip_tag_name(elem.tag)
        if elem.tag == "page":
            if containsSpecialTitle(str(elem.find("title").text), "Wikipedia:", "Template:", "Draft:", "Module:", "Portal:", "Help:", "File:", "Category:"):
                elem.clear()
                continue

            pageCount += 1
            parsePage(elem, db)
            elem.clear()
            if not pageCount % 100000:
                elapsed_time = time.time() - start_time
                print("{} articles parsed".format((pageCount/100000)*100000), end=" ")
                print("Elapsed time: {}".format(hms_string(elapsed_time)))

    elapsed_time = time.time() - start_time

    print("Elapsed time: {}".format(hms_string(elapsed_time)))

def test():
    with open("sample.txt", encoding="utf-8") as fin:


        page = wtp.parse(fin.read())
        print(type(page))

        infobox = getTemplate(page, "Infobox")
        if inCategories(page, "births"):
            print("aa")
            if infobox is None:
                return
            infobox = infobox[infobox.find("\n") + 1: infobox.rfind("\n")]
            if infobox.count("\n") == 0:  # One line infobox creates an infinite loop
                return
            infobox = wtp.Table(infobox)

            # Iterate over every cell and parse it
            d = defaultdict(list)
            for a in range(len(infobox.cells())):
                for b in range(len(infobox.cells(row=a))):
                    parsed = parseCell(str(infobox.cells(row=a, column=b)))
                    d[parsed[0]] = parsed[1]


if __name__ == "__main__":
    main(pathWikiXML)
    #test()


