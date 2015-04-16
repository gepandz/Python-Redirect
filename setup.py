try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'George Pandzik',
        'url': 'http://github.com/gepandz/NAME',
        'download_url': 'git://github.com/gepandz/NAME',
        'author_email': 'nope@uhuh.net',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname',
}

setup(**config)
