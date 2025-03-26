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

from ..metadata import (
    ObservationHeader,
    SpatialReferenceHeader,
    TemporalReferenceHeader,
    VODFFormatHeader,
)
from ..references import Ref

__all__ = ["EventList"]


class EventList(BinaryTable):
    """VODF Level-1 Event List HDU."""

    class __header__(
        BinaryTableHeader,
        VODFFormatHeader,
        SpatialReferenceHeader,
        TemporalReferenceHeader,
        ObservationHeader,
    ):
        EXTNAME = HeaderCard(allowed_values=["event-list"], type_=str)
        EXTLEVEL = HeaderCard(
            type_=int,
            description=(
                "the level in a hierarchy of extension levels of the extension header containing it. "
                "The value shall be 1for the highest level; levels with a higher value of this "
                "keyword shall be subordinate to levels with a lower value"
            ),
            reference=Ref.fits_v4,
            allowed_values=range(1, 10),
        )
        HDUCLAS1 = HeaderCard(
            allowed_values="OGIP", description="OGIP-compatible", reference=Ref.ogip
        )
        HDUCLAS2 = HeaderCard(
            allowed_values="EVENTS",
            description="event-list table",
            reference=Ref.ogip,
        )

    # Mandatory Columns
    EVENT_ID = Int64(
        description="ID of this event, unique within an observation",
    )

    TIME = Double(
        description="Event time of arrival, as an MET",
        unit=u.s,
        ucd="time",
        reference=Ref.ogip_event_lists,
    )

    RA_RECO = Double(
        description="Reconstructed Right Ascension of event point-of-origin.",
        unit=u.deg,
        ucd="pos.eq.ra;stat.fit",
        reference=Ref.ogip_event_lists,
    )

    DEC_RECO = Double(
        description="Reconstructed Declination of event point-of-origin",
        unit=u.deg,
        ucd="pos.eq.dec;stat.fit",
        reference=Ref.ogip_event_lists,
    )

    # TODO: how to deal with non-energy-like energy proxies (like n_hits)
    ENERGY_RECO = Double(
        description=(
            "Reconstructed event energy, or proxy for that value. "
            "This value can be folded through the IRF to measure true energy"
        ),
        unit=u.TeV,
        ucd="phys.energy;stat.fit",
        reference=Ref.ogip_event_lists,
    )
