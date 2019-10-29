from bs4 import BeautifulSoup
import urllib.request,time,csv,datetime,pytz
choice=input('Enter anime name: ')
with open('schedule.csv', 'r', newline='') as csvfile:
    spamwriter=csv.reader(csvfile, delimiter=',')
    for row in spamwriter:
        if choice == row[0]:
            name=row[0]
            day=row[1]
            showtime=row[2]
            break
with open('data.csv', 'r', newline='') as csvfile:
    spamwriter=csv.reader(csvfile, delimiter=',')
    for row in spamwriter:
        if name == row[1]:
            link="https://horriblesubs.info"+row[2]
            print("FOUND")
            break
######datetime.datetime.now(pytz.timezone("US/Pacific"))
current_time=str(datetime.datetime.now(pytz.timezone("US/Pacific")))[11:16]

while True:
    if current_time==showtime:
        print("grab the mag links")
        break
    current_time=str(datetime.datetime.now(pytz.timezone("US/Pacific")))[11:16]

        
print(current_time)
