import datetime

def getUrl():
    today = datetime.date.today()
    mondayDate = today - datetime.timedelta(days=today.weekday())
    return mondayDate
