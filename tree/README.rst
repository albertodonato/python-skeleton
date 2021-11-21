${project.title}
================

|Latest Version| |Build Status| |Coverage Status| |Documentation|

Description of ${project.title}...


Documentation
-------------

Documentation is available on ReadTheDocs_.


Installation
------------

${project.name} can be installed from PyPI_.

As a user run::

  $$ pip install ${project.name}


Development installation
------------------------

The source tree is available available at `<${project.url}>`_, users should
install Virtualenv_ for development.

As a user run::

  $$ virtualenv <target-dir>
  $$ . <target-dir>/bin/activate
  $$ git clone ${project.url}.git
  $$ cd ${project.name}
  $$ pip install -e .


.. _ReadTheDocs: https://${project.name}.readthedocs.io/en/latest/
.. _PyPI: https://pypi.python.org/
.. _Virtualenv: https://virtualenv.pypa.io/

.. |Latest Version| image:: https://img.shields.io/pypi/v/${project.name}.svg
   :alt: Latest Version
   :target: https://pypi.python.org/pypi/${project.name}
.. |Build Status| image:: ${project.url}/workflows/CI/badge.svg
   :alt: Build Status
   :target: ${project.url}/actions?query=workflow%3ACI
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/albertodonato/${project.name}/main.svg
   :alt: Coverage Status
   :target: https://codecov.io/gh/albertodonato/${project.name}
.. |Documentation| image:: https://readthedocs.org/projects/${project.name}/badge/?version=stable
   :alt: Documentation
   :target: https://${project.name}.readthedocs.io/en/stable/?badge=stable
