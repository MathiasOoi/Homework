import wikitextparser as wtp
from collections import defaultdict
def getTemplate(page, template):
    """
    Given a parsed article return the string of given template
    :param page: 'wikitextparser._wikitext.WikiText'
    :param template: String (first part of a template)
    :return: String of Template
    """
    for tm in page.templates:
        if str(tm).split("\n")[0].strip("{").startswith(template):
            return str(tm)
s = """| honorific_suffix    = {{post-nominals|CBE}}
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
"""

with open("sample.txt", encoding="utf-8") as fin:
    parsed = wtp.parse(fin.read())
    infobox = getTemplate(parsed, "Infobox")
    # Remove first and last line of infobox by slicing
    infobox = infobox[infobox.find("\n") + 1: s.rfind("\n")]
    infobox = wtp.Table(infobox)
    for a in range(len(infobox.cells())):
         for b in range(len(infobox.cells(row=a))):
             print(infobox.cells(row=a, column=b), end="")
#     p = wtp.Table("""
# | honorific_suffix    = {{post-nominals|CBE}}
# | alt                 = Gilmour playing onstage
# | caption             = Gilmour performing in 2015
# | birth_name          = David Jon Gilmour
#     """)
#
#     for i in parsed.templates:
#         print(i)
#         print()
#         if "{{Infobox" in i:
#             x = wtp.Table(s)
#             #print(x.cells())
#
#
#     #for a in range(len(p.cells())):
#     #    for b in range(len(p.cells(row=a))):
#     #        print(p.cells(row=a, column=b), end="")






