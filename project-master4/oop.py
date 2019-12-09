from bs4 import BeautifulSoup
import urllib.request,time,csv,datetime,pytz
import releaseschedulescraper, new_release_magscrape


class Anime:
    def __init__(self,showid,title,showlink,release_time):
        self.showid=showid
        self.title=title
        self.showlink=showlink
        self.release_time=release_time
        self.res=input("Enter desired resolution: ")

objects=[]


    
choice=input('Enter anime name: ')
choice=choice.lower()
with open('schedule.csv', 'r', newline='') as csvfile:
    spamwriter=csv.reader(csvfile, delimiter=',')
    for row in spamwriter:
        title=row[0].replace(" ","")
        if  choice.replace(" ","") ==title.lower() :
            name=row[0]
            day=row[1]
            showtime=row[2]
            break
with open('data.csv', 'r', newline='') as csvfile:
    spamwriter=csv.reader(csvfile, delimiter=',')
    for row in spamwriter:
        if name == row[1]:
            link="https://horriblesubs.info"+row[2]
            showid=row[0]
            print("FOUND") #CALL ANOTHER SCRIPT HERE "new_release_magscrape.py"
            generic=Anime(showid,name,link,(day,showtime))
            objects.append(generic)
            all_res=new_release_magscrape.latest_scrape(showid)
            break
        
##########datetime.datetime.now(pytz.timezone("US/Pacific"))
####current_time=str(datetime.datetime.now(pytz.timezone("US/Pacific")))[11:16]
####today=datetime.datetime.now(pytz.timezone("US/Pacific")).strftime("%A")
####
######release_time=(day,showtime)
####
####while True:
####    if today==day and current_time==showtime:
####        all_res=new_release_magscrape.latest_scrape(showid)
####        print(all_res)
####        break
####    current_time=str(datetime.datetime.now(pytz.timezone("US/Pacific")))[11:16]
####    today=datetime.datetime.now(pytz.timezone("US/Pacific")).strftime("%A")
####
####print(current_time)
####