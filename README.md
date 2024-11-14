# Bump'X: Bump and release versions

[![Build Status](https://github.com/datagouv/bumpx/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/datagouv/bumpx/actions/workflows/main.yml)
![PyPI - Last version](https://img.shields.io/pypi/v/bumpx)
![PyPI - License](https://img.shields.io/pypi/l/bumpx)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bumpx)

Bump'X is a version bumper and releaser forked from [Bump'R](https://github.com/datagouv/bumpx).
In a single CLI command, Bump'X can:

- Clean-up release artifact
- Bump version and tag it
- Build a source distribution and upload on PyPI
- Update version for a new development cycle

Bump'X intend to be customizable with the following features:

- Optional test suite run before bump
- Customizable with a config file
- Overridable by command line
- Extensible with hooks

## Compatibility

Bump'X requires Python `>=3.7` (and `<4.0`)

## Installation

You can install Bump'X with pip:

```bash
pip install bumpr
```

## Usage

You can use directly the command line to setup every parameter:

```bash
bumpr fake/__init__.py README.rst -M -ps dev
```

But Bump'X is designed to work with a configuration file (`bumpr.rc` by defaults).
Some features are only availables with the configuration file like:

- commit message customization
- hooks configuration
- multiline test, clean and publish commands

Here's an exemple:

```ini
[bumpr]
file = fake/__init__.py
vcs = git
tests = tox
publish = python setup.py sdist register upload
clean =
    python setup.py clean
    rm -rf *egg-info build dist
files = README.rst

[bump]
unsuffix = true
message = Bump version {version}

[prepare]
suffix = dev
message = Prepare version {version} for next development cycle

[changelog]
file = CHANGELOG.rst
bump = {version} ({date:%Y-%m-%d})
prepare = In development

[readthedoc]
id = fake
```

This way you only have to specify which part you want to bump on the
command line:

```bash
bumpr -M  # Bump the major
bumpr     # Bump the default part aka. patch
```

## Documentation

The documentation for the upstream project [Bump'R](https://github.com/noirbizarre/bumpr) is hosted on Read the Docs:

- [Stable](https://bumpr.readthedocs.io/en/stable/) [![Stable documentation status](https://readthedocs.org/projects/bumpr/badge/?version=stable)](https://bumpr.readthedocs.io/en/stable/?badge=stable)
- [Development](https://bumpr.readthedocs.io/en/latest/) [![Latest documentation Status](https://readthedocs.org/projects/bumpr/badge/?version=latest)](https://bumpr.readthedocs.io/en/latest/?badge=latest)
