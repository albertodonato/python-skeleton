from pathlib import Path

from setuptools import (
    find_packages,
    setup,
)


tests_require = ['pytest']

config = {
    'name': '${project.name}',
    'version': '0.0.1',
    'license': 'GPLv3+',
    'description': '${project.title}',
    'long_description': Path('README.rst').read_text(),
    'author': '${author.name}',
    'author_email': '${author.email}',
    'maintainer': '${author.name}',
    'maintainer_email': '${author.email}',
    'url': '${project.url}',
    'download_url': '${project.download-url}',
    'packages': find_packages(
        include=['${project.base}','${project.base}.*']),
    'include_package_data': True,
    'entry_points': {'console_scripts': []},
    'test_suite': '${project.base}',
    'install_requires': [],
    'tests_require': tests_require,
    'extras_require': {'testing': tests_require},
    'keywords': '',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python :: 3 :: Only']}

setup(**config)
