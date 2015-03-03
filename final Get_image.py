import urllib 
import mechanize 
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib
import urllib2
import os
        
search = "apple"
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent','Mozilla')]

htmltext = browser.open("https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1414&bih=709&q="+search+"&oq="+search)
img_urls = []
formatted_images = []
soup = BeautifulSoup(htmltext)
results = soup.findAll("img")
for r in results:
    img_urls.append(r["src"])

image_type = "Action"

for img in img_urls:
  raw_img = urllib2.urlopen(img).read()
  #add the directory for your image here 
  DIR="/home/shuchita/googlePics/"
  cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
  print cntr
  f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
  f.write(raw_img)
  f.close()
