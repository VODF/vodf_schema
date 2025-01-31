#!/usr/bin/env python3

"""Common metadata headers for VODF."""

from astropy import units as u
from fits_schema import Header, HeaderCard

from .references import CITE
from .version import __version__ as vodf_version

URL = "https://PUT_VODF_DOCUMENTATION_URL_FOR_THIS_VERSION_HERE/"

__all__ = [
    "VODFFormat",
    "ReferencePosition",
]


class VODFFormat(Header):
    """Required headers for VODF HDUs."""

    HDUCLASS = HeaderCard(allowed_values="VODF")
    HDUDOC = HeaderCard(allowed_values=URL, case_insensitive=False)
    HDUVERS = HeaderCard(allowed_values={vodf_version})


class ReferencePosition(Header):
    """Reference position of the observatory, for time and coordinates.

    This version of VODF supports only Earth-centered locations.
    """

    TREFPOS = HeaderCard(
        description="Code for the spatial location at which the observation time is valid",
        reference=CITE["fits_v4"],
        type_=str,
        allowed_values=["TOPOCENTER"],
    )

    OBSGEO_B = HeaderCard(
        keyword="OBSGEO-B",
        description="the latitude of the observation, with North positive",
        type_=float,
        unit=u.deg,
        ucd="pos.earth.lat",
        reference=CITE["fits_v4"],
    )
    OBSGEO_L = HeaderCard(
        keyword="OBSGEO-L",
        description="the longitide of the observation, with East positive",
        type_=float,
        unit=u.deg,
        ucd="pos.earth.lon",
        reference=CITE["fits_v4"],
    )
    OBSGEO_H = HeaderCard(
        keyword="OBSGEO-H",
        description="the altitude of the observation",
        type_=float,
        unit=u.m,
        ucd="pos.earth.altitude",
        reference=CITE["fits_v4"],
    )


# ======================================================================
#  Copied from GADF so far, need to update:


class CoordinateSystem(Header):
    """Coordinate system definition."""

    EQUINOX = HeaderCard(
        description="Coordinate epoch. Optional since implied by RADECSYS",
        reference=CITE["fits_v4"],
        type_=float,
        unit=u.yr,
        allowed_values=2000.0,
        required=False,
    )
    RADECSYS = HeaderCard(
        description="Coordinate stellar reference frame",
        reference=CITE["fits_v4"],
        type_=str,
        allowed_values={"ICRS", "FK5"},
    )


class TimeDefinition(Header):
    """Header keywords for the definition of time columns."""

    # All keywords are required here. Add this to the headerschema when a table
    # contains a time column

    MJDREFI = HeaderCard(required=True, type_=int)
    MJDREFF = HeaderCard(required=True, type_=float)
    TIMEUNIT = HeaderCard(required=True, type_=str, allowed_values=["s"])
    TIMESYS = HeaderCard(
        required=True, type_=str, allowed_values=["UT1", "UTC", "TAI", "TT"]
    )
    TIMEREF = HeaderCard(
        required=True,
        type_=str,
        allowed_values=[
            "LOCAL",
            "SOLARSYSTEM",
            "HELIOCENTRIC",
            "GEOCENTRIC",
        ],
    )


class Object(Header):
    """Name and coordinates of observerd object, if any."""

    OBJECT = HeaderCard(required=False, type_=str)
    RA_OBJ = HeaderCard(required=False, type_=float)
    DEC_OBJ = HeaderCard(required=False, type_=float)


class DataProductHeaders(Header):
    """Identify this HDU."""

    DATE = HeaderCard(
        description="Date of HDU creation",
        type_=str,
        reference=CITE["fits_v4"],
    )


class ObservationHeaders(Header):
    """Describes an observation."""


class CreatorHeaders(Header):
    """The creator of this data product."""

    ORIGIN = HeaderCard(
        description="Organization or institution responsible for this file",
        type_=str,
        reference=CITE["fits_v4"],
        examples=["CTAO", "KM3Net"],
    )

    CREATOR = HeaderCard(
        description="Name of software used to create this file",
        reference=CITE["heasarc"],
    )
