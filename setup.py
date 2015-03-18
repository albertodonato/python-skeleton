#
# This file is part of $title.

# $title is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# $title is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with $title.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

from $name import __version__, __doc__ as description


config = {
    'name': '$name',
    'version': __version__,
    'license': 'GPLv3+',
    'description': description,
    'long_description': open('README.rst').read(),
    'author': 'Alberto Donato',
    'author_email': 'alberto.donato@gmail.com',
    'maintainer': 'Alberto Donato',
    'maintainer_email': 'alberto.donato@gmail.com',
    'url': 'https://bitbucket.org/ack/$name',
    'download_url': 'https://bitbucket.org/ack/$name/downloads',
    'packages': find_packages(exclude=['*.test.*', '*.test', 'test.*']),
    'include_package_data': True,
    'entry_points': {'console_scripts': []},
    'test_suite': '$name',
    'install_requires': [],
    'tests_require': [],
    'keywords': '',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python']}

setup(**config)
