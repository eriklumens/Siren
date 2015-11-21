import urllib
from datetime import date

media_types = ['artists', 'labels', 'masters']
base_url = 'http://data.discogs.com.s3-us-west-2.amazonaws.com/data/'
today = date.today()
date = '%s%s%s' % (today.year, today.month, "01")

for media_type in media_types:
    url = base_url + 'discogs_%s_%s.xml.gz' % (date, media_type)

    print 'Downloading %s for %s' % (media_type, date)
    urllib.urlretrieve(url, filename="data/%s_%s.xml.gz" % (media_type, date))
    print '%s downloaded succesfully' % media_type
    print 40 * '='
