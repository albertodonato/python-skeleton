${project.title}
================

Description of ${project.title}...

`documentation <${project.doc-url}>`_ |
`sources <${project.url}>`_ |
`issues <${project.issues-url}>`_


Install
-------

${project.title} can be installed from `PyPI <https://pypi.python.org/>`_.

As a user run::

  $$ pip install ${project.name}


Development installation
------------------------

The source tree is available available at
`<${project.url}>`_, users should install `Virtualenv
<https://virtualenv.pypa.io/>`_ for development.

As a user run::

  $$ virtualenv <target-dir>
  $$ . <target-dir>/bin/activate
  $$ git clone ${project.url}.git
  $$ cd ${project.name}
  $$ python setup.py develop
