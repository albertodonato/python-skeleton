python-skeleton
===============

Helper script to setup a typical python project.

It takes a few config options and generates a tree with template/boilerplate
files for further customization.


Usage
-----

- edit the ``project.yaml`` with personal and project details
- run

  $$ python-skeleton/project -C project.yaml bootstrap <destdir>

- ``cd destdir`` and edit generated files there and add code
- optionally, run

  $$ python-skeleton/project -C project.yaml license <destdir> <patterns>

to add or update the copyright notice at the beginning of files matching the
specified patterns.

A typical usage would be passing ``Makefile '*.py'`` as patterns.

  
**Note**: You can edit ``project.list`` to change which files are included in
 the generation.
