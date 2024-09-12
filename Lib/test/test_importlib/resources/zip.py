"""
Generate zip test data files.
"""

import zipfile

from test.test_zipfile._path.test_path import add_dirs


def make_zip_file(tree, dst):
    """
    Zip the files in tree into a new zipfile at dst.
    """
    with zipfile.ZipFile(dst, 'w') as zf:
        for name, contents in walk(tree):
            zf.writestr(name, contents)
        add_dirs(zf)
    return dst


def walk(tree, prefix=''):
    for name, contents in tree.items():
        if isinstance(contents, dict):
            yield from walk(contents, prefix=f'{prefix}{name}/')
        else:
            yield f'{prefix}{name}', contents
