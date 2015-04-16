try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Script that talks to a database and returns an HTTP redirect',
        'author': 'John and George Pandzik',
        'url': 'http://github.com/jspandz/redirect',
        'download_url': 'git://github.com/jspandz/redirect',
        'author_email': 'jspandz@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['redirect'],
        'scripts': [],
        'name': 'redirect',
}

setup(**config)
