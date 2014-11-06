import urllib2
import re

def check_for_update():
    new = get_current_article()
    old = get_last_article()
    return new == old

def get_current_article():
    req = urllib2.Request('http://disneyparks.disney.go.com/blog/category/disneyland-resort/')
    response = response = urllib2.urlopen(req)
    page = response.read()

    raw_articles = re.findall(r'<div class="post-title">\n\t+<h1><a href="http://disneyparks.disney.go.com/blog/[0-9]+/[0-9]+/[a-z-]+/" rel="bookmark" title="[A-Za-z0-9:!-()\', ]+">[A-Za-z0-9:!-()\', ]+', page)
    striped = raw_articles[0][45:]
    endOfUrl = striped.find('"')
    url = striped[:endOfUrl]
    nextDesiredIndex = endOfUrl + 42
    striped = striped [nextDesiredIndex:]
    endOfTitle = striped.find('"')
    title = striped[:endOfTitle]
    return { "title" : title,
             "url" : url }

def get_last_article():
    pass

def send_message():
    pass
