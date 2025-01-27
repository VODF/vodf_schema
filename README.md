# vodf_schema

An implementation of the VODF FITS file format schema using the
[fits_schema](https://github.com/VODF/fits_schema) package.

This package will provide:

- self-documenting schema definitions
- a validation api and command-line tool capable of checking existing FITS files
  for compliance with VODF

## Development

### Editable installations

Editable installations in this setup rely on PEP 660 (see above), support was
introduced in `pip` 21.3 (released 2021-10) and setuptools 64.0 (released
2022-08). The setuptools version is required in `pyproject.toml`.

To install in editable mode, use

```
$ pip install -e .
```

you can add extras, e.g. for developing and building the docs, use

```
$ pip install -e '.[dev,doc,test]'
```

or just

```
$ pip install -e '.[all]'
```

Keep in mind that editable installations have limitations as to what changes can
take effect automatically without rerunning `pip install -e .`. Python code
changes to existing files take effect, but for example adding new entry-points,
changes to the source code of compiled extensions etc. will require rerunning
the installation.

See <https://setuptools.pypa.io/en/latest/userguide/development_mode.html#limitations>

## Docs

Build the documentation in html format using:

```
$ make -C docs html
```

To view them, you can run:

```
$ python -m http.server -d docs/build/html
```

You can also install `sphinx-autobuild` and run

```
sphinx-autobuild docs docs/build/html
```

to get a continuously running and updating preview of the docs while you edit them.
