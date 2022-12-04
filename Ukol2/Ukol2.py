def get_stackoverflow(query):
    import urllib, urllib.request as urllib2, re, urllib.parse as urlparse
    params = urllib.urlencode({'q': query, 'sort': 'relevance'})
    html = urllib2.urlopen("http://stackoverflow.com/search?%s" % params).read()
    links = re.findall(r'<h3><a href="([^"]*)" class="answer-title">([^<]*)</a></h3>', html)
    links = [(urlparse.urljoin('http://stackoverflow.com/', url), title) for url,title in links]

    return links
