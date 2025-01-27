#!/usr/bin/env python3

"""VODF Level 1 data model."""

from astropy import units as u
from fits_schema import BinaryTable, BinaryTableHeader, Double, HeaderCard, Int16, Int64

from .metadata import FormatSpec, ReferencePosition


class EventList(BinaryTable):
    """VODF Level-1 Event List HDU."""

    class __headers__(BinaryTableHeader, FormatSpec, ReferencePosition):
        HDUCLAS1 = HeaderCard(allowed_values="OGIP", description="OGIP-compatible")
        HDUCLAS2 = HeaderCard(allowed_values="EVENTS", description="event-list table")

        # OBS_ID   = HeaderCard(type_=int)
        # TSTART   = HeaderCard(type_=float)
        # TSTOP    = HeaderCard(type_=float)
        # ONTIME   = HeaderCard(type_=float)
        # LIVETIME = HeaderCard(type_=float)
        # DEADC    = HeaderCard(type_=float)
        # RA_PNT   = HeaderCard(type_=float)
        # DEC_PNT  = HeaderCard(type_=float)
        # ORIGIN   = HeaderCard(type_=str)
        # TELESCOP = HeaderCard(type_=str)
        # INSTRUME = HeaderCard(type_=str)
        # CREATOR  = HeaderCard(type_=str)

    # Mandatory
    EVENT_ID = Int64()
    TIME = Double(unit=u.s)
    RA = Double(unit=u.deg)
    DEC = Double(unit=u.deg)
    ENERGY = Double(unit=u.TeV)

    # Optional
    MULTIP = Int16(required=False)
    GLON = Double(unit=u.deg, required=False)
    GLAT = Double(unit=u.deg, required=False)
    ALT = Double(unit=u.deg, required=False)
    AZ = Double(unit=u.deg, required=False)
    DETX = Double(unit=u.deg, required=False)
    DETY = Double(unit=u.deg, required=False)
    THETA = Double(unit=u.deg, required=False)
    PHI = Double(unit=u.deg, required=False)
    DIR_ERR = Double(unit=u.deg, required=False)
    ENERGY_ERR = Double(unit=u.TeV, required=False)
    COREX = Double(unit=u.m, required=False)
    COREY = Double(unit=u.m, required=False)
    CORE_ERR = Double(unit=u.m, required=False)
    XMAX = Double(unit=u.g / u.cm**2, required=False)
    XMAX_ERR = Double(unit=u.g / u.cm**2, required=False)
    HIL_MSW = Double(required=False)
    HIL_MSL = Double(required=False)
    HIL_MSL_ERR = Double(required=False)
