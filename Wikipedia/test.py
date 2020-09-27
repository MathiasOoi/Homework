import wikitextparser as wtp


with open("sample.txt") as fin:
    parsed = wtp.parse(fin.read())
    p = wtp.Table("""
| honorific_suffix    = {{post-nominals|CBE}}
| alt                 = Gilmour playing onstage
| caption             = Gilmour performing in 2015
| birth_name          = David Jon Gilmour
    """)
    for i in parsed.templates:
        if "{{Infobox" in str(i):
            print(i)
            break

