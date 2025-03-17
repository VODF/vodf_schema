#!/usr/bin/env python3

"""Common info for all VODF HDUs."""

from fits_schema import (
    BinaryTable,
    BinaryTableHeader,
    HeaderCard,
    Int64,
    String,
)

from .metadata import VODFFormatHeader
from .references import Ref


class GroupingTable(BinaryTable):
    """A FITS Hieararchical Grouping table."""

    class __headers__(BinaryTableHeader, VODFFormatHeader):
        EXTNAME = HeaderCard(allowed_values="GROUPING")

    MEMBER_LOCATION = String(
        description="URI of file containing member HDU",
        required=False,
        reference=Ref.fits_grouping,
    )
    MEMBER_NAME = String(
        description="EXTNAME keyword from the group member’s header.",
        reference=Ref.fits_grouping,
    )
    MEMBER_VERSION = Int64(
        description=(
            "An integer to be used to distinguish among different extensions "
            "in a FITS file with the same type and name, i.e., "
            "the same values for XTENSION and EXTNAME. "
        ),
        reference=Ref.fits_grouping,
    )
    MEMBER_LOCATION = String(
        description=(
            "The location of the group member’s FITS file using Uniform Resource "
            "Identifiers. If the FITS file resides on the same computer system as the group "
            "table, then partial URIs may be used instead of absolute URIs. If the group "
            "member resides in the same FITS file as the group table, or the MEMBER LOCATION "
            "value becomes invalid then this field may be filled with the FITS null value "
            "appropriate for the column type. "
        ),
        reference=Ref.fits_grouping,
        required=False,
    )
    MEMBER_URI_TYPE = String(
        description=(
            "Contains the mnemonic for the Uniform Resource Identifier type "
            "used in the corresponding MEMBER LOCATION field. Recommended values "
            "for this column field are 'URL' for the Uniform Resource Locator and "
            "'URN' for the Uniform Resource Name."
        ),
        reference=Ref.fits_grouping,
        required=False,
    )
