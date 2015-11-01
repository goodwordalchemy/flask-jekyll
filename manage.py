import os, shutil
from datetime import datetime
from app import create_app, freezer, pages
from flask.ext.script import Manager, Shell, prompt_bool

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def freeze(debug=False):
    if debug:
        freezer.run(debug=True)
    freezer.freeze()

from config import basedir
pagesdir = os.path.join(basedir, 'app/pages')

@manager.command
def new_post(title):
    """
    creates a new file in 'pages' directory with 
    indicated title, formatted yaml header, and opens
    new file in sublime text editor
    """
    
    yaml_header = 'title: %s' % title + '\n' +\
                  'date: %s' % datetime.now()[:-7] + '\n\n'
    
    filename = title.replace(' ','_') + '.md'
    filepath = os.path.join(pagesdir, filename)
    with open(filepath, 'w') as thefile:
        thefile.write(yaml_header)
    os.system("subl %s" % filepath)

@manager.command
def publish(push=False, remote='origin', branch='master'):
    """adds blog post pages in root directory to git staging, commits, 
    and optionally those blog posts to github"""
    freezer.freeze()

    for page in pages:
        os.system('git add %s' % page.path)
    os.system('git add %s' % os.path.join(basedir,'app/pages/'))
    for page in pages:
        os.system('git add %s' % os.path.join(basedir, page.path))
    os.system('git commit -m "publishing articles %s"' % ' '.join(
            [page.path for page in pages]))
    if push or prompt_bool(
            "push from branch '%s' to remote '%s'? [y]" % (remote, branch)):
        os.system('git push %s %s' % (remote, branch))

@manager.command
def remove(filename, push=False, remote='origin', branch='master'):
    """removes a blog post completely from the system"""
    try: 
        filepath = os.path.join(basedir,'app/pages/%s.md'%filename)
        os.remove(filepath)
        os.system('git add -u %s' % filepath)
    except OSError: print  '"%s.md" does not exist or has been removed' % filename
    try: 
        dirpath = os.path.join(basedir, filename)
        shutil.rmtree(dirpath)
        os.system('git add -u  %s' % dirpath)
    except OSError: print '"%s" does not exist or has been removed'
    os.system('git commit -m "removed %s"'%filename)
    if push or prompt_bool(
            "push from branch '%s' to remote '%s'? [y]" % (remote, branch)):
        os.system('git push %s %s' % (remote, branch))

if __name__ == '__main__':
    manager.run()
