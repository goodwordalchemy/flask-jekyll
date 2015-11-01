title: How I made this Site (Github Pages and Flask Static Sites)
date: 2015-10-30 12:00:00

I tried using Jekyll before, but Jekyll is written in Ruby, so it was hard for me to customize or even hack with not knowing Ruby.  So that's why I made this static blog generator using Flask.  

I just finished reading the book [Flask Web Development](https://www.safaribooksonline.com/library/view/flask-web-development/9781491947586/) by Miguel Grinberg, which is a really amazing resource just just for learning flask but for learning web development in general.  

Basically, armed with the knowledge I gained through building the example social blogging app that they build in that book, I refactored the code described and linked to in [this tutorial](http://stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/) by Steven Loria, where he  goes through how to configure Flask-Frozen and Flask-Flat-Pages for use on a github pages site.

That's pretty much it.  Then I followed the directions on the [github pages site](https://pages.github.com/)

Actually, that's not quite it.  I started using the site and I realized that it was kindof annoying to make the new files every time, and to go through the whole freeze.py and git workflow every time I wanted to add or edit an article, so I added a bunch of convenience commands using [Flask-script](https://flask-script.readthedocs.org/en/latest/).  Check out the readme for Flask-jekyll