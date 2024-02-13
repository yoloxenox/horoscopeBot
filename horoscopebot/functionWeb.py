import re
import requests
import locale
import hashlib

import functionTime as ftt
import functionText as fte

def functionGorafi():

    reList = ["Poissons", "Sagittaire", "Verseau", "Furet", "Capricorne", "Bélier"]
    clean = ["</strong>", "</p>", "/>", "&nbsp;"]

    messageList = []
    message = txtToClean = txtCleaned = ""
    txtToClean = ""

    request = RequestLoader()
    r = requests.get(request)

    if r.status_code == 200:
        try: 
            for item in reList:
                reg = f'{ item } :.*'
                txtToClean = re.findall(reg, r.text)
                txtCleaned = fte.cleaner(clean, txtToClean)
                messageList.append(txtCleaned)
                message = "\n".join(messageList)
        except IndexError: 
            message = f'Désolé, la requête : {request} a échouée'
        except:
            message = "Désolé quelque chose s'est mal passé"
    return message
    with open('url.txt', 'w') as f:
        f.write(request)

def webScrapeGoraficlean():
    txtToClean = txtCleaned = ""
    request = f'https://www.legorafi.fr/category/horoscope-2/'
    r = requests.get(request)

    pattern = "if\(is_iframe\){iframe_count\+=1}}}\).*$"
    reg = f'{pattern}'
    txtToClean = re.findall(reg, r.text)
    txtCleaned = fte.cleaner(txtToClean, r.text)
    return txtCleaned

def webScrapeGorafichksm():

    checksum = hashlib.sha256(webScrapeGoraficlean().encode('utf-8')).hexdigest()
    with open('chksmGorafi.txt', 'w') as f:
        f.write(checksum)

def isChksumDifferent():
    f = open("chksmGorafi.txt", "r")
    oldChecksum = f.read()
    newChecksum = hashlib.sha256(webScrapeGoraficlean().encode('utf-8')).hexdigest()
    if oldChecksum == newChecksum:
        return False
    else :
        return True
    
def RequestLoader():
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    Date = ftt.getDate()
    m = Date.strftime('%m')
    M = Date.strftime("%B")
    newRequest = f'https://www.legorafi.fr/{ Date.year }/{ m }/{ Date.day }/horoscope-du-{ Date.day }-{ M }-{ Date.year }/'
    newRequest = newRequest.replace("é","e")
    f = open("url.txt", "r")
    oldRequest = f.read()
    if newRequest ==  oldRequest:
        request = oldRequest
        return request
    else:
        request = newRequest
        return request