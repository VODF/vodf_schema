#!/usr/bin/env python3

"""VODF Level 1 EventList HDU Definition."""

from astropy import units as u
from fits_schema import (
    BinaryTable,
    BinaryTableHeader,
    Double,
    HeaderCard,
    Int64,
)

from ..metadata import SpatialReferenceHeader, TemporalReferenceHeader, VODFFormatHeader
from ..references import CITE

__all__ = ["EventList"]


class EventList(BinaryTable):
    """VODF Level-1 Event List HDU."""

    class __header__(
        BinaryTableHeader,
        VODFFormatHeader,
        SpatialReferenceHeader,
        TemporalReferenceHeader,
    ):
        EXTNAME = HeaderCard(allowed_values=["event-list"], type_=str)
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
        reference=CITE["ogip_event_lists"],
    )
    RA = Double(
        description="Reconstructed Right Ascension of event point-of-origin.",
        unit=u.deg,
        ucd="pos.eq.ra;stat.fit",
        reference=CITE["ogip_event_lists"],
    )
    DEC = Double(
        description="Reconstructed Declination of event point-of-origin",
        unit=u.deg,
        ucd="pos.eq.dec;stat.fit",
        reference=CITE["ogip_event_lists"],
    )
    ENERGY = Double(
        description="Reconstructed event energy",
        unit=u.TeV,
        ucd="phys.energy;stat.fit",
        reference=CITE["ogip_event_lists"],
    )
