# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blog', 'blog.migrations', 'blog.templatestags']

package_data = \
{'': ['*'], 'blog': ['templates/blog/*']}

install_requires = \
['django>=3.1,<4.0']

setup_kwargs = {
    'name': 'blog',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Santosh Magar',
    'author_email': 'mgrsantox@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
