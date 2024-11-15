# Bump'X: Bump and release versions

[![Build Status](https://github.com/datagouv/bumpx/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/datagouv/bumpx/actions/workflows/main.yml)
![PyPI - Last version](https://img.shields.io/pypi/v/bumpx)
![PyPI - License](https://img.shields.io/pypi/l/bumpx)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/bumpx)

Bump'X is a version bumper and releaser forked from [Bump'R](https://github.com/noirbizarre/bumpr).
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

Bump'X requires Python `>=3.9` (and `<4.0`).

Bump'X also requires that you have [git CLI](https://git-scm.com/) and [GitHub CLI](https://cli.github.com/) installed on your system.

## Installation

You can install Bump'X with pip:

```bash
pip install bumpx
```

## Usage

You can use directly the command line to setup every parameter:

```bash
bumpx fake/__init__.py README.rst -M -ps dev
```

But Bump'X is designed to work with a configuration file (`bumpr.rc` by defaults).
Some features are only availables with the configuration file like:

- commit message customization
- hooks configuration
- multiline test, clean and publish commands

Here's an exemple:

```ini
[bumpx]
file = fake/__init__.py
vcs = git
forge = github
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
bumpx -M  # Bump the major
bumpx     # Bump the default part aka. patch
```

If you use GitHub as a forge and publish release on it, you might have to specify which origin should be used to publish the releases, with:

```bash
gh repo set-default
```

## Documentation

The documentation for the upstream project [Bump'X](https://github.com/datagouv/bumpx) is hosted on Read the Docs:

- [Stable](https://bumpr.readthedocs.io/en/stable/) [![Stable documentation status](https://readthedocs.org/projects/bumpr/badge/?version=stable)](https://bumpr.readthedocs.io/en/stable/?badge=stable)
- [Development](https://bumpr.readthedocs.io/en/latest/) [![Latest documentation Status](https://readthedocs.org/projects/bumpr/badge/?version=latest)](https://bumpr.readthedocs.io/en/latest/?badge=latest)
