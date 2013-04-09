# To print titles of top 10 in r/aww
import urllib
from ReddiWrap import ReddiWrap

# Create new ReddiWrap instance
reddit = ReddiWrap()
aww = reddit.get('/r/aww')

topten = aww[:10]
for p in topten:
    image = urllib.urlopen("http://site.com/image.jpg").read()
    print p.url, p.title
