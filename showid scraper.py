from bs4 import BeautifulSoup
import urllib.request, time, re, csv,random
#User agent settings
#    req = urllib.request.Request(
#        url='https://horriblesubs.info/shows',
#        data=None,
#        headers={
#            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#        }
#    )

req = urllib.request.Request(url='https://horriblesubs.info/shows',headers={'User-Agent': 'Mozilla/5.0'}) 
f = urllib.request.urlopen(req)
soup = BeautifulSoup(f, features="html.parser")
shows = soup.find_all("div", "ind-show")

with open('data.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(["showid","title","showlink"])
    for i in shows:
        for x in i.find_all("a", href=True):
            print(x.text)
            showlink=x.get("href")
            print(showlink)
            gotoshow = urllib.request.Request(url=('https://horriblesubs.info'+showlink),headers={'User-Agent': 'Mozilla/5.0'})
            try:
                showsource=urllib.request.urlopen(gotoshow)
                stew = BeautifulSoup(showsource, features="html.parser")
                showid = (stew.find(string=re.compile('hs_showid')))[16:-1]
                print(showid)
                #file.write("\n"+showid+x.text)
                spamwriter.writerow([showid,x.text,showlink])
                #time.sleep(random.randint(0,5))
            except urllib.error.HTTPError:
                spamwriter.writerow(["ERROR404",x.text,showlink])
                
#file.close()
print("DONE")


##        with open('data.csv','w') as csvFile:
##            writer=csv.writer(csvFile)
##            writer.writerow(showid)
##        csvFile.close()
