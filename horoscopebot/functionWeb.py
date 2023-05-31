import re
import requests
import functionTime as ft
import locale

def cleaner(clean, txt):
    txt = txt[0]
    for item in clean:
        txt = re.sub(item, "", txt)
    return txt

def functionGorafi():
    locale.setlocale(locale.LC_ALL,'fr_FR.utf8')

    reList = ["Poissons", "Sagittaire", "Verseau", "Furet", "Capricorne"]
    clean = ["</strong>", "</p>", "/>"]
    request = ""

    mD = ft.getUrl()
    m = mD.strftime('%m')
    M = mD.strftime("%B")
    messageList = []
    message = txtToClean = txtCleaned = ""
    txtToClean = ""

    request = f'https://www.legorafi.fr/{ mD.year }/{ m }/{ mD.day }/horoscope-du-{ mD.day }-{ M }-{ mD.year }/'
    r = requests.get(request)

    if r.status_code == 200:
        for item in reList:
            reg = f'{ item } :.*'
            txtToClean = re.findall(reg, r.text)
            txtCleaned = cleaner(clean, txtToClean)
            messageList.append(txtCleaned)
            message = "\n".join(messageList)
    return message
            