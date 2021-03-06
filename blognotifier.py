import urllib2
import re

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

def get_last_article_title():
    file = open('article_titles.txt', 'r')
    article_titles = file.read()
    file.close()
    article_titles = article_titles.split('\n')
    last_article = article_titles[len(article_titles) - 1]
    return last_article

def append_new_article(article_title):
    with open('article_titles.txt', 'a') as file:
        file.write("\n" + article_title)

def send_message(article):
    pass

# MAIN: 

current_article = get_current_article()
current_article_title = current_article['title']

last_article_title = get_last_article_title()

if current_article_title != last_article_title:
    append_new_article(current_article_title)
    send_message(current_article)
