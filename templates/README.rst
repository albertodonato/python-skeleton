{{ project.title }}
{{ '=' * project.title | length }}

|Latest Version| |Build Status| |PyPI Downloads|


.. |Latest Version| image:: https://img.shields.io/pypi/v/{{ project.name }}.svg
   :alt: Latest Version
   :target: https://pypi.python.org/pypi/{{ project.name }}
.. |Build Status| image:: {{ project.urls['Source Code'] }}/actions/workflows/ci.yaml/badge.svg?branch=main
   :alt: Build Status
   :target: {{ project.urls['Source Code'] }}/actions?query=workflow%3ACI
.. |PyPI Downloads| image:: https://static.pepy.tech/badge/{{ project.name }}/month
   :alt: PyPI Downloads
   :target: https://pepy.tech/projects/{{ project.name }}
