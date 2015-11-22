from datetime import date
import gzip
import urllib
import os

media_types = ['artists', 'labels', 'masters']
base_url = 'http://data.discogs.com.s3-us-west-2.amazonaws.com/data/'
today = date.today()
date = '%s%s%s' % (today.year, today.month, "01")

for media_type in media_types:
    filename = '%s_%s.xml' % (date, media_type)
    url = base_url + 'discogs_%s.gz' % filename

    print 'Downloading %s for %s' % (media_type, date)
    urllib.urlretrieve(url, filename="data/%s.gz" % filename)
    print '%s downloaded succesfully' % media_type
    print 40 * '-'

    print 'Unpacking %s' % media_type
    outF = open('data/%s' % filename, 'wb')
    inF = gzip.open('data/%s.gz' % filename, 'rb')
    tmp_f = inF.read()
    outF.write(tmp_f)
    outF.close()
    inF.close()
    os.remove('data/%s.gz' % filename)
    print '%s unpacked succesfully' % media_type
    print 40 * '='
    print ''
