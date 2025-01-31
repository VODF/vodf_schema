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
    EVENT_ID = Int64(
        description="ID of this event, unique within an observation",
    )
    TIME = Double(
        description="Event time of arrival, as an MET",
        unit=u.s,
        ucd="time",
    )
    RA = Double(
        description="Reconstructed Right Ascension of event point-of-origin.",
        unit=u.deg,
        ucd="pos.eq.ra;stat.fit",
    )
    DEC = Double(
        description="Reconstructed Declination of event point-of-origin",
        unit=u.deg,
        ucd="pos.eq.dec;stat.fit",
    )
    ENERGY = Double(
        description="Reconstructed event energy",
        unit=u.TeV,
        ucd="phys.energy;stat.fit",
    )
