from bs4 import BeautifulSoup
import urllib.request,time,csv
req=urllib.request.Request(url="https://horriblesubs.info/release-schedule/",
                           headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
soup = BeautifulSoup((urllib.request.urlopen(req)), features="html.parser")
noodles=(soup.find_all("a",title="See all releases for this show"))
scrapedtimes=soup.find_all(class_="schedule-time")
days=soup.find_all(class_="weekday")
titles=[]
times=[]
join=[]
daycounter=0
weekdays=["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for i in days:
    print((i.text)[0:9])
for i in noodles:
    titles.append(i.text)
actual_times=[]
for i in range(0,len(scrapedtimes)):
    times.append(weekdays[daycounter])
    actual_times.append(scrapedtimes[i].text)
    if i!=len(scrapedtimes)-1:
        if int((scrapedtimes[i].text)[:1])>int((scrapedtimes[i+1].text)[:1]):
            daycounter+=1                
for i in range(0,len(titles)):
    join.append([titles[i],times[i],actual_times[i]])
print(join)

with open('schedule.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(["showname","day","time"])
    for i in join:
        spamwriter.writerow(i)


#return choice
