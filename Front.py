# To print titles of top 10 in r/aww
import urllib

from ReddiWrap import ReddiWrap

# Create new ReddiWrap instance
reddit = ReddiWrap()
front = reddit.get('/r/all')

topten = front[:10]
for p in topten:
    print p.title
