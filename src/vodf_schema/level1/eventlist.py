#!/usr/bin/env python3

"""VODF Level 1 EventList HDU Definition."""

from astropy import units as u
from fits_schema import (
    BinaryTable,
    Double,
    HeaderCard,
    Int64,
)

from ..metadata import ReferencePosition, VODFFormat
from ..references import CITE

__all__ = ["EventList"]


class EventList(BinaryTable):
    """VODF Level-1 Event List HDU."""

    class __headers__(VODFFormat, ReferencePosition):
        HDUCLAS1 = HeaderCard(
            allowed_values="OGIP", description="OGIP-compatible", reference=CITE["ogip"]
        )
        HDUCLAS2 = HeaderCard(
            allowed_values="EVENTS",
            description="event-list table",
            reference=CITE["ogip"],
        )

    # Mandatory Columns
    EVENT_ID = Int64()
    TIME = Double(unit=u.s)
    RA = Double(unit=u.deg)
    DEC = Double(unit=u.deg)
    ENERGY = Double(unit=u.TeV)
