from setuptools import setup

name = "types-ipaddress"
description = "Typing stubs for ipaddress"
long_description = '''
## Typing stubs for ipaddress

This is a PEP 561 type stub package for the `ipaddress` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `ipaddress`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/ipaddress. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `9f869723509ac027bae6b6f567b921d6a229e8ec`.
'''.lstrip()

setup(name=name,
      version="1.0.1",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['ipaddress-python2-stubs'],
      package_data={'ipaddress-python2-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
