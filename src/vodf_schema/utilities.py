#!/usr/bin/env python3

"""Some helpers for working with schemas using astropy Tables and Jupyter Notebooks."""

import re
from collections import defaultdict

from astropy.table import Table
from fits_schema import BinaryTable, Header, HeaderCard
from fits_schema.schema_element import _REFERENCE_SET

__all__ = ["display_bintable", "get_references", "headers_to_table", "columns_to_table"]


def get_references(as_dict=False):
    """Retucrn the reference list from all currently imported schemas."""
    references = {r: i for i, r in enumerate(_REFERENCE_SET)}

    if as_dict:
        return references

    return Table(
        dict(citation=list(references.values()), reference=list(references.keys()))
    )


def _extract_references(table: BinaryTable):
    references = get_references(as_dict=True)
    table["citation"] = [references.get(r, None) for r in table["reference"]]
    del table["reference"]
    return table


def columns_to_table(bintable: BinaryTable) -> Table:
    """Make a table of the columns of a BinaryTable schema."""
    output_cols = [
        "name",
        "required",
        "unit",
        "ucd",
        "description",
        "ndim",
        "shape",
        "reference",
    ]

    input_cols = bintable.__columns__.values()
    data = defaultdict(list)
    for outcol in output_cols:
        for incol in input_cols:
            data[outcol].append(getattr(incol, outcol))

    table = Table(data)
    return _extract_references(table)


def headers_to_table(header: Header, cards: list[HeaderCard] | None = None) -> Table:
    """Make a table of the cards of a header."""
    if not cards:
        cards = header.__cards__.values()

    output_cols = [
        "keyword",
        "required",
        "allowed_values",
        "unit",
        "ucd",
        "description",
        "reference",
        "examples",
        "ivoa_name",
    ]

    data = defaultdict(list)
    for outcol in output_cols:
        for card in cards:
            data[outcol].append(getattr(card, outcol))

    table = Table(data)
    table.meta["description"] = header.__doc__
    return _extract_references(table)


def split_camel(name):
    """Reformat CamelCase into separate words."""
    if name is None:
        return ""
    return " ".join(
        re.sub("([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", name)).split()
    )


def display_bintable(hdu):
    """Display a bintable in a notebook."""
    from IPython.display import HTML, display

    display(HTML(f"<h1>{hdu.__name__}</h1>"))
    display(HTML(f"<p>{hdu.__doc__}</p>"))
    display(HTML("<h2>Headers</h2>"))

    for header, cards in hdu.__header__.grouped_cards().items():
        hdr_table = headers_to_table(header, cards.values())

        if header.__name__ != "__header__":
            display(
                HTML(
                    f"<h3>{split_camel(header.__name__)}</h3> <p><b>{hdr_table.meta['description']}</p>"
                )
            )
        display(hdr_table)

    display(HTML("<h2>Columns</h2>"))
    display(columns_to_table(hdu))

    display(HTML("<h1>References</h1>"))
    display(get_references())
