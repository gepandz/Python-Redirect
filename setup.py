try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Script that talks to a database and returns an HTTP redirect',
        'author': 'John and George Pandzik',
        'url': 'http://github.com/jspandz/Python-Redirect',
        'download_url': 'git://github.com/jspandz/Python-Redirect',
        'author_email': 'jspandz@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['Python-Redirect'],
        'scripts': [],
        'name': 'Python-Redirect',
}

setup(**config)
