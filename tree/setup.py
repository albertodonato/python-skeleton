#
# This file is part of ${project.title}.
#
# ${project.title} is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# ${project.title} is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ${project.title}.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

from ${project.name} import __version__, __doc__ as description


config = {
    'name': '${project.name}',
    'version': __version__,
    'license': 'GPLv3+',
    'description': description,
    'long_description': open('README.rst').read(),
    'author': '${author.name}',
    'author_email': '${author.email}',
    'maintainer': '${author.name}',
    'maintainer_email': '${author.email}',
    'url': '${project.url}',
    'download_url': '${project.download-url}',
    'packages': find_packages(),
    'include_package_data': True,
    'entry_points': {'console_scripts': []},
    'test_suite': '${project.name}',
    'install_requires': [],
    'tests_require': [],
    'keywords': '',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python']}

setup(**config)
