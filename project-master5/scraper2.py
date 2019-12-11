from bs4 import BeautifulSoup
import urllib.request,time,csv,re

req=urllib.request.Request(url="https://horriblesubs.info/release-schedule/",
                           headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
soup = BeautifulSoup((urllib.request.urlopen(req)), features="html.parser")
                                    
noodles=(soup.find_all("a",title="See all releases for this show"))
scrapedtimes=soup.find_all(class_="schedule-time")
titles=[]
times=[]
links=[]
join=[]
daycounter=0
weekdays=["Monday",'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for i in noodles:
    links.append(i.get("href"))
    titles.append(i.text)
    
actual_times=[]
for i in range(0,len(scrapedtimes)):
    times.append(weekdays[daycounter])
    actual_times.append(scrapedtimes[i].text)
    if i!=len(scrapedtimes)-1:
        if int((scrapedtimes[i].text)[:1])>int((scrapedtimes[i+1].text)[:1]):
            daycounter+=1    








with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(["showid","showname","showlink"])
    for x in noodles:
        #print(x.text)
        showlink=x.get("href")
        print(showlink)
        gotoshow = urllib.request.Request(url=('https://horriblesubs.info'+showlink),headers={'User-Agent': 'Mozilla/5.0'})
        try:
            showsource=urllib.request.urlopen(gotoshow)
            stew = BeautifulSoup(showsource, features="html.parser")
            showid = (stew.find(string=re.compile('hs_showid')))[16:-1]
            #print(showid)
            #file.write("\n"+showid+x.text)
            spamwriter.writerow([showid,x.text,showlink])
            #time.sleep(random.randint(0,5))
        except urllib.error.HTTPError:
            spamwriter.writerow(["ERROR404",x.text,showlink])

