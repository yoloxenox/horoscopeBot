import re

def cleaner(clean, txt):
    txt = txt[0]
    for item in clean:
        txt = re.sub(item, "", txt)
    return txt
