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
    file = open('article_titles.txt', 'r')
    article_titles = file.read()
    file.close()
    article_titles = article_titles.split('\n')
    print len(article_titles)
    print article_titles
    last_article = article_titles[len(article_titles) - 1]
    print last_article
    pass

def send_message():
    pass
