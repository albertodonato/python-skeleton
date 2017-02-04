python-skeleton
===============

Helper script to setup a typical python project.

It takes a few config options and generates a tree with template/boilerplate
files for further customization.


Usage
-----

- copy the ``project.yaml.template`` to ``project.yaml`` and edit it with
  personal and project details.
- run ``python-skeleton/project -C project.yaml bootstrap <destdir>``
- ``cd destdir``, edit generated files as needed and add actual project files.
- optionally, run ``python-skeleton/project -C project.yaml license <destdir>
  <patterns>`` to add or update the copyright notice at the beginning of files
  matching the specified patterns.
  A typical invocation would pass ``Makefile '*.py'`` as patterns.


*Note*: You can edit ``project.list`` to change which files are included in the
generation.
