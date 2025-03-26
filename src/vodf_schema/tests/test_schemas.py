#!/usr/bin/env python3

"""Test schemas.

These tests may seem trivial or simple, but the schema validation happens on
import, so this tests that the schemas are correctly written and that there is
no `vodf_schema.exceptions.SchemaError`.
"""


def test_import_level1():
    """Test the schemas defined in level1.py."""
    from vodf_schema import level1

    assert level1.EventList  # just to prevent pre-commit from removing the import


def test_import_level2():
    """Test the schemas defined in level1.py."""
    from vodf_schema import level2

    assert level2.__name__  # just to prevent pre-commit from removing the import


def test_import_level3():
    """Test the schemas defined in level1.py."""
    from vodf_schema import level3

    assert level3.__name__  # just to prevent pre-commit from removing the import


def test_import_metadata():
    """Test the schemas defined in level1.py."""
    from vodf_schema import metadata

    assert (
        metadata.VODFFormatHeader
    )  # just to prevent pre-commit from removing the import


def test_import_hdus():
    """Test the schemas defined in level1.py."""
    from vodf_schema import hdu

    assert hdu.GroupingTable  # just to prevent pre-commit from removing the import
