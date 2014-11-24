BlogNotifier
============

This script downloads the page disneyparksblog.com/category/disneyland-resort,
then it parses the html to find the title and URL for the first article on the page.
Next it checks to see if that first article, the current article, has the same title
as the last article by looking up the title of the last article in a txt file.  
If the titles do not match the new article is appended to the file and a notification
message is sent to alert the user that there is a new article.
