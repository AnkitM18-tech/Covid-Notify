from plyer import notification
import requests
from bs4 import BeautifulSoup



def notifyMe(title, message):
    notification.notify(
        title = title,
        message =message,
        app_icon = "D:\GitHub\Covid-Notify\covid-19.ico",
        timeout = 5 
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    my_HTML_data = getData("https://www.mohfw.gov.in/")
    soup = BeautifulSoup(my_HTML_data,'html.parser')