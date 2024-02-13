import datetime

def getDate():
    today = datetime.date.today()
    Date = today - datetime.timedelta(days=today.weekday())
    return Date
