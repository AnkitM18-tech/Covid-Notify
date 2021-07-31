from plyer import notification
import requests
from bs4 import BeautifulSoup



def notifyMe(title, message):
    notification.notify(
        title = title,
        message =message,
        app_icon = "D:\GitHub\Covid-Notify\covid-19.ico",
        timeout = 15 
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    my_HTML_data = getData("https://www.mygov.in/corona-data/covid19-statewise-status")
    soup = BeautifulSoup(my_HTML_data,'html.parser')
    # print(soup.prettify())
    divLookup = ["div.field-name-field-select-state","div.field-name-field-total-confirmed-indians","div.field-name-field-cured","div.field-name-field-deaths"]
    StateName = []
    Confirmed = []
    Cured = []
    Deaths = []
    for item in soup.select(divLookup[0]):
        StateName.append(item.get_text().replace(u'\xa0', u' '))

    for item in soup.select(divLookup[1]):
        # pass
        Confirmed.append(item.get_text().replace(u'\xa0', u' '))


    for item in soup.select(divLookup[2]):
        # pass
        Cured.append(item.get_text().replace(u'\xa0', u' '))


    for item in soup.select(divLookup[3]):
        # pass
        Deaths.append(item.get_text().replace(u'\xa0', u' '))

    x = zip(StateName,Confirmed,Cured,Deaths)
    x = list(x)
    for stat in x:
        stateName,totalConfirmed,totalCured,totalDeaths = stat
        if stateName in ['State Name: Odisha','State Name: Andhra Pradesh'] :  # Can add other states
            print(stat)
            nTitle = "COVID-19 Info"
            nText = f"{stateName}  {totalConfirmed}  {totalCured}  {totalDeaths}"
            notifyMe(nTitle, nText)