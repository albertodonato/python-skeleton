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
