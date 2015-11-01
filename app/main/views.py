from flask import render_template
from . import main
from .. import pages, freezer


@main.route('/')
def home():
    posts = [page for page in pages]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)

@main.route('/<path:path>/')
def page(path):
    # 'path is the filename of a page, without the file extension'
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

