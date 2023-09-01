# Skeleton tree for Python projects

[![Build status](https://github.com/albertodonato/python-skeleton/workflows/CI/badge.svg)](https://github.com/albertodonato/python-skeleton/actions?query=workflow%3ACI)


This is a helper script to setup a typical Python project.

It takes a few config options and generates a tree with template/boilerplate
files for further customization.


Usage
-----

- edit `project-template.yaml` with project details.

- run `./python-skeleton project.yaml <destdir>`

- go into `<destdir>`, edit generated files as needed and add actual project
  files.


To re-generate files for an existing project (e.g. when template is updated),
it's also possible to pass the project `pyproject.toml` file as source for the
metadata.
