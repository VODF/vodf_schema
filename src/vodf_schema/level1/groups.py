#!/usr/bin/env python3

"""VODF Level 1 data model."""

from ..hdu import GroupingTable

__all__ = ["ObservationGroupingTable", "IRFGroupingTable"]


class ObservationGroupingTable(GroupingTable):
    """Groups all HDUs related to an observation."""

    pass


class IRFGroupingTable(GroupingTable):
    """Groups all HDUs that form a complete IRF."""

    pass
