#!/usr/bin/env python3
# Licensed un a 3-clause BSD-style license - see LICENSE

"""The minimum contents of a "Observation HDU".

- Headers: Observation, DataRelease, and ObservationCollection

- Bintable: a grouping table containing the links (URI) to the HDUs of that
observation to its associated EventList, Pointing, OnTime , IRF HDUs ... qThe
sub-HDUs in the group may or may not be included, and could be fetched
separately (e.g. if the URI points to a new file)
"""

from fits_schema import BinaryTableHeader, HeaderCard

from ..hdu import GroupingTable
from ..metadata import (
    ObservationHeader,
    SpatialReferenceHeader,
    TemporalReferenceHeader,
    VODFFormatHeader,
)


class Observation(GroupingTable):
    """Defines what HDUs link to a single observation."""

    class __header__(
        VODFFormatHeader,
        BinaryTableHeader,
        ObservationHeader,
        SpatialReferenceHeader,
        TemporalReferenceHeader,
    ):
        EXTNAME = HeaderCard(allowed_values=["OBSERVATION"])
