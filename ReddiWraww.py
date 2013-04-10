# To print titles of top 10 in r/aww
import urllib
from ReddiWrap import ReddiWrap
from datetime import datetime

def getUTCTime(timestamp_string):
    return datetime.utcfromtimestamp(timestamp_string)

def getTime(timestamp_string):
    return datetime.fromtimestamp(timestamp_string)

# Create new ReddiWrap instance
reddit = ReddiWrap()
aww = reddit.get('/r/aww')
strFormat = "%Y-%m-%d"

topten = aww[:10]

print "Title", "|", "Time", "|", "Votes + -"
for p in topten:
    #image = urllib.urlopen("http://site.com/image.jpg").read()
    #print p.url, p.title
    print "=", p.title, "="
    print "Votes | +:", p.upvotes, "-:", p.downvotes, "fuzzy:", p.score
    print "Time[Local]:", getTime(p.created) ,"Time[UTC]:", getUTCTime(p.created_utc)
    print
