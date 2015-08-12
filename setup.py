try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Cloudflare Wrapper',
    'author': 'Tim Sherwood',
    'url': 'https://github.com/0snug0/cloudconnect',
    'download_url': 'https://github.com/0snug0/cloudconnect/archive/master.zip',
    'author_email': 'tim@dualmediasolutions.com',
    'version': '0.1',
    'install_requires': ['nose', 'requests>=2.3.0',],
    'packages': ['cloudconnect'],
    'scripts': [],
    'name': 'cloudconnect',
}

setup(**config)
