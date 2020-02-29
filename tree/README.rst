${project.title}
================

|Latest Version| |Build Status| |Coverage Status| |Documentation Status|

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
  $$ python3 setup.py develop


.. _ReadTheDocs: https://${project.name}.readthedocs.io/en/latest/
.. _PyPI: https://pypi.python.org/
.. _Virtualenv: https://virtualenv.pypa.io/

.. |Latest Version| image:: https://img.shields.io/pypi/v/${project.name}.svg
   :target: https://pypi.python.org/pypi/${project.name}
.. |Build Status| image:: https://img.shields.io/travis/albertodonato/${project.name}.svg
   :target: https://travis-ci.com/albertodonato/${project.name}
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/albertodonato/${project.name}/master.svg
   :target: https://codecov.io/gh/albertodonato/${project.name}
.. |Documentation Status| image:: https://readthedocs.org/projects/${project.name}/badge/?version=stable
   :target: https://${project.name}.readthedocs.io/en/stable/?badge=stable
