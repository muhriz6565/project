from bs4 import BeautifulSoup
import urllib.request
##while soup!="DONE":
##    soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url="https://horriblesubs.info/api.php?method=getshows&type=show&showid="+str(showid)+"&nextid="+str(nextid),
##                            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})),
##                         features="html.parser")
##    nextid+=1
##    print(soup)
#https://horriblesubs.info/api.php?method=getshows&type=show&showid=###&nextid=###

def latest_scrape(showid):
    latest=[]
    req=(urllib.request.urlopen(urllib.request.Request(url="https://horriblesubs.info/api.php?method=getshows&type=show&showid="+str(showid)+"&nextid=0",
                            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})))
    soup = BeautifulSoup((req), features="html.parser")
    for thing in (soup.find_all('a')):
        if (thing.get("href"))[0:7]=="magnet:":
            latest.append(thing.get("href"))
            #print(len(thing.get("href")))
            #print("\n\n\n")
            if len(latest)==3:
                return latest
                break
print(latest_scrape(53))
        
