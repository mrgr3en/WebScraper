from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://akis.tallinn.ee/kogunemised/xml/23d381ce')
soup = BeautifulSoup(r.data, 'lxml')
counter = 0
places = soup.kogunemised.findAll("toimumiskoht")
events = soup.kogunemised.findAll("nimetus")
time = soup.kogunemised.findAll("toimumise_aeg")
def innerLoop():
    for date in time:
        print(time[counter-1].text)
        for place in places:
            print(places[counter-1].text)
            return
    
for event in events:
    counter +=1
    print(str(counter) + ".üritus")
    print(event.text)
    innerLoop()
        
