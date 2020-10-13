import wikitextparser as wtp

def getCategories(page):
    s = page.get_sections()[-1].string
    categories = s[s.find("[[Category:"):].split("\n")
    return categories

with open("test.txt", encoding="utf-8") as fin:
    page = wtp.parse(fin.read())
    categories = getCategories(page)
    for c in categories:
            print(repr(categories))
