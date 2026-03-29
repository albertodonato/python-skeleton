# Skeleton tree for Python projects

[![Build status](https://github.com/albertodonato/python-skeleton/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/albertodonato/python-skeleton/actions?query=workflow%3ACI+branch%3Amain)

This is a helper script to setup a Python project.

It takes a few config options and generates a tree with template/boilerplate
files for further customization.


Usage
-----

- edit `project-template.yaml` with project details.

- run `tox -- --project-details project-template.yaml <project-dir>`

- go into `<project-dir>`, edit generated files as needed and add actual project
  files.

To update files for an existing project, avoid passing `--project-details`, in
which case project details will be found from the existing project tree.  This
will require comparing the diff and restoring intentional changes.
