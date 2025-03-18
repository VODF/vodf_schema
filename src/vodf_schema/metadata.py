#!/usr/bin/env python3

"""Common metadata headers for VODF."""

from astropy import units as u
from fits_schema import Header, HeaderCard

from .references import Ref
from .version import __version__ as vodf_version

URL = "https://PUT_VODF_DOCUMENTATION_URL_FOR_THIS_VERSION_HERE/"

__all__ = [
    "VODFFormatHeader",
    "SpatialReferenceHeader",
]


class VODFFormatHeader(Header):
    """Required headers for VODF HDUs."""

    HDUCLASS = HeaderCard(allowed_values="VODF")
    HDUDOC = HeaderCard(allowed_values=URL, case_insensitive=False)
    HDUVERS = HeaderCard(allowed_values={vodf_version})


class SpatialReferenceHeader(Header):
    """Reference position of the observatory, for time and coordinates.

    This version of VODF supports only Earth-centered locations.
    """

    TREFPOS = HeaderCard(
        description="Code for the spatial location at which the observation time is valid",
        reference=Ref.fits_v4,
        type_=str,
        allowed_values=["TOPOCENTER"],
    )

    OBSGEO_B = HeaderCard(
        keyword="OBSGEO-B",
        description="the latitude of the observation, with North positive",
        type_=float,
        unit=u.deg,
        ucd="pos.earth.lat",
        reference=Ref.fits_v4,
    )
    OBSGEO_L = HeaderCard(
        keyword="OBSGEO-L",
        description="the longitide of the observation, with East positive",
        type_=float,
        unit=u.deg,
        ucd="pos.earth.lon",
        reference=Ref.fits_v4,
    )
    OBSGEO_H = HeaderCard(
        keyword="OBSGEO-H",
        description="the altitude of the observation",
        type_=float,
        unit=u.m,
        ucd="pos.earth.altitude",
        reference=Ref.fits_v4,
    )


class TemporalReferenceHeader(Header):
    """Defines the reference time, to which all time columns in the HDU are relative."""

    # TODO: do we really need to split MJDREF into (I/F) parts? Is that level of
    # precision required?
    MJDREFI = HeaderCard(
        description="the integer part of reference time in MJD",
        reference=Ref.fits_v4,
        type_=int,
        unit="d",
    )
    MJDREFF = HeaderCard(
        description="the fractional part of reference time in MJD",
        reference=Ref.fits_v4,
        type_=float,
        unit="d",
    )
    DATEREF = HeaderCard(
        required=False,
        description="String representation of the reference time in ISO-8601 format",
        reference=Ref.fits_v4,
        type_=str,
        examples=["2025-01-01 00:00:00"],
    )

    # TODO: Is TIMEUNIT necessary? Time columns must have a unit field, so this
    # may be redundant. It would only be useful for header values.
    TIMEUNIT = HeaderCard(
        description=(
            "the time unit that shall apply to all time instances and durations "
            "that do not have an implied time unit (e.g. the JD, MJD epochs)."
        ),
        required=False,
        reference=Ref.fits_v4,
        type_=str,
        allowed_values=["s"],
    )

    TIMESYS = HeaderCard(
        description="the time scale of the time-related keywords. For simulated data, use LOCAL.",
        reference=Ref.fits_v4,
        type_=str,
        allowed_values=["TT", "UTC", "UT1", "TAI", "GPS", "LOCAL"],
    )
    TREFPOS = HeaderCard(
        description="spatial location at which the observation time is valid.",
        reference=Ref.fits_v4,
        type_=str,
        allowed_values=[
            "TOPOCENTER",
            "GEOCENTER",
            "BARYCENTER",
            "RELOCATABLE",
            "CUSTOM",
        ],
    )
    TIMEDEL = HeaderCard(
        required=False,
        description="time resolution in the units of TIMEUNIT, useful for binned time-series.",
        type_=float,
    )


class ObservationHeader(Header):
    """Describes an observation."""

    DATE_OBS = HeaderCard(
        "DATE-OBS",
        type_=str,
        description="Human-readable observation start date, in UTC and ISO format",
        examples=["2025-01-01 15:34:21"],
        reference=Ref.fits_v4,
    )
    TELESCOP = HeaderCard(
        type_=str,
        description="Observatory or telescope used to make the observation",
        examples=["CTAO", "Km3Net", "SWGO"],
        reference=Ref.fits_v4,
        ivoa_name="ObsCore.facility_name",
    )
    INSTRUME = HeaderCard(
        type_=str,
        required=False,
        description="Subarray or instrument on the TELESCOP used to make the observation.",
        reference=Ref.fits_v4,
        ivoa_name="ObsCore.instrument_name",
    )

    OBS_ID = HeaderCard(ivoa_name="obs_id")

    # TODO: missing other things from ObsCore/CTAO observation context


class BibliographicHeader(Header):
    """The creator of this data product."""

    ORIGIN = HeaderCard(
        description="Organization or institution responsible for this file.",
        type_=str,
        reference=Ref.fits_v4,
        examples=["CTAO ERIC"],
    )

    # TODO: we also need the software version, etc.  Is CREATOR still useful?
    CREATOR = HeaderCard(
        description="Name of software used to create this file", reference=Ref.heasarc
    )

    REFERENC = HeaderCard(
        required=False,
        description=(
            "reference where the data associated with the header are published. "
            "It is recommended that either the 19-digit bibliographic identifier8 used in "
            "the Astrophysics Data System bibliographic databases (http://adswww.harvard.edu/) "
            "or the Digital Object Identifier (http://doi.org)"
        ),
        examples=["1994A&AS..103..135A", "’doi:10.1006/jmbi.1998.2354"],
        reference=Ref.fits_v4,
    )


class FixityHeader(Header):
    """Headers to ensure data integrity."""

    DATASUM = HeaderCard(
        type_=int,
        description=(
            "unsigned-integer value of the 32-bit ones’ complement checksum of the "
            "data records in the HDU (i.e., excluding the header records)"
        ),
        reference=Ref.fits_v4,
    )
    CHECKSUM = HeaderCard(
        type_=int,
        description=(
            "ASCII character string whose value forces the 32-bit ones’ "
            "complement checksum accumulated over the entire FITS HDU to equal negative 0. "
        ),
        reference=Ref.fits_v4,
    )


# ======================================================================
#  Copied from GADF so far, need to update:


class CoordinateSystemHeader(Header):
    """Coordinate system definition."""

    EQUINOX = HeaderCard(
        description="Coordinate epoch. Optional since implied by RADECSYS",
        reference=Ref.fits_v4,
        type_=float,
        unit=u.yr,
        allowed_values=2000.0,
        required=False,
    )
    RADECSYS = HeaderCard(
        description="Coordinate stellar reference frame",
        reference=Ref.fits_v4,
        type_=str,
        allowed_values={"ICRS", "FK5"},
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
        reference=Ref.fits_v4,
    )
