import zlib
from wikidb import *
import wikitextparser as wtp

db = WikiDB("wiki.db")

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

def getInfobox(page):
    article = wtp.parse(page)
    infobox = getTemplate(article, "Infobox")
    print(infobox)
    print(type(infobox))


for (pageid, title, categories, article) in db.iterRandom(1):
    print(title)
    print(getInfobox(article))
