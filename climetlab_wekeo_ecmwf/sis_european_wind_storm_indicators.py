#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations
from climetlab.decorators import normalize

from climetlab_wekeo_ecmwf.main import Main


class sis_european_wind_storm_indicators(Main):
    name = "EO:ECMWF:DAT:SIS_EUROPEAN_WIND_STORM_INDICATORS"
    dataset = "EO:ECMWF:DAT:SIS_EUROPEAN_WIND_STORM_INDICATORS"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "product",
        "time_aggregation",
        "spatial_aggregation",
        "spatial_aggregation",
        "year",
        "month",
        "day",
    ]

    @normalize(
        "product",
        [
            "loss_indicators",
            "risk_indicators",
            "summary_indicators",
            "windstorm_footprints",
            "windstorm_tracks",
        ],
        multiple=True,
    )
    @normalize(
        "time_aggregation",
        [
            "annual",
            "decadal",
        ],
        multiple=True,
    )
    @normalize(
        "spatial_aggregation",
        [
            "austria",
            "belgium",
            "czech_republic",
            "denmark",
            "estonia",
            "finland",
            "france",
            "germany",
            "ireland",
            "italy",
            "latvia",
            "lithuania",
            "luxemburg",
            "netherlands",
            "norway",
            "poland",
            "portugal",
            "spain",
            "sweden",
            "switzerland",
            "united_kingdom",
        ],
        multiple=True,
    )
    @normalize(
        "spatial_aggregation",
        [
            "agriculture",
            "europe",
            "european_nuts1_region",
            "european_nuts3_region",
            "industry",
            "other",
            "residential",
            "transport",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1979",
            "1980",
            "1981",
            "1982",
            "1983",
            "1984",
            "1985",
            "1986",
            "1987",
            "1988",
            "1989",
            "1990",
            "1991",
            "1992",
            "1993",
            "1994",
            "1995",
            "1996",
            "1997",
            "1998",
            "1999",
            "2000",
            "2001",
            "2002",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2020",
            "2021",
        ],
        multiple=True,
    )
    @normalize(
        "month",
        [
            "01",
            "02",
            "03",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "day",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "all",
        ],
    )
    @normalize(
        "format_",
        [
            "tgz",
            "zip",
        ],
    )
    def __init__(
        self,
        product,
        time_aggregation,
        spatial_aggregation,
        spatial_aggregation,
        year,
        month,
        day,
        variable="all",
        format_,
    ):
        super().__init__(
            product=product,
            time_aggregation=time_aggregation,
            spatial_aggregation=spatial_aggregation,
            spatial_aggregation=spatial_aggregation,
            year=year,
            month=month,
            day=day,
            variable=variable,
            format_=format_,
        )