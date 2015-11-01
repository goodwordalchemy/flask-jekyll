This is a static site blog like Jekyll for Github pages, but it uses python and flask instead of ruby to generate the static pages.

##Installation

1. clone the repo
2. set up virtual environment: `virtualenv venv`
3. activate vitual environment: `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. This one's a little tricky.  If you want to use this generator to set up your own github pages website:
    1. delete the .git folder for this repo (`rm -rf .git`)
    2. reimplement .git folder using direction on the [github pages site](https://pages.github.com/)

##Use
There are some convenience commands that I've made for generating new blog posts, publishing blog posts to your github, and removing posts.  The source code for these commands is in the 'manage.py' file.

* to generate pages: `python manage.py new_post <post title, for example: "First Post">`.  This command assumes that you have the `subl` command line command set up to launch sublime text.

* to publish your blog pages: `python manage.py publish`.  This command will create a bunch of new directories in your root directory.  Those are the html files that are going to be served on github pages.  You will be prompted for whether to push your changes.

* to remove a page: `python manage.py remove <page to remove (without extension), eg: 'shitty-post'>`
