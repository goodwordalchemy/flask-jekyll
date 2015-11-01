import os

basedir = os.path.abspath(os.path.dirname(__file__))
def parent_dir(path):
        '''Return the parent of a directory.'''
        return os.path.abspath(os.path.join(path, os.pardir))

class Config:
    REPO_NAME = "goodwordalchemy.github.io"  # Used for FREEZER_BASE_URL
    DEBUG = True

    APP_DIR = os.path.join(basedir,'app')

    PROJECT_ROOT = basedir
    # In order to deploy to Github pages, you must build the static files to
    # the project root
    FREEZER_DESTINATION = PROJECT_ROOT
    # Since this is a repo page (not a Github user page),
    # we need to set the BASE_URL to the correct url as per GH Pages' standards
    FREEZER_BASE_URL = "http://localhost/"
    FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                        # will be deleted when you run the freezer
    FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
    FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
    FLATPAGES_EXTENSION = '.md'

    @staticmethod
    def init_app(app):
        pass

config = {
    'default': Config
}