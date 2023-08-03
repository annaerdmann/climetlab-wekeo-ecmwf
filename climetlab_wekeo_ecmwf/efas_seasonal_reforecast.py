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


class efas_seasonal_reforecast(Main):
    name = "EO:ECMWF:DAT:EFAS_SEASONAL_REFORECAST"
    dataset = "EO:ECMWF:DAT:EFAS_SEASONAL_REFORECAST"

    choices = [
        "variable",
        "model_levels",
        "format_",
    ]

    string_selects = [
        "leadtime_hour",
        "soil_level",
        "hmonth",
        "hyear",
    ]

    @normalize(
        "hmonth",
        [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
        ],
        multiple=True,
    )
    @normalize(
        "hyear",
        [
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
            "2003",
            "2004",
            "2005",
            "2006",
            "2007",
            "2008",
            "2009",
            "2010",
            "2011",
            "2012",
            "2013",
            "2014",
            "2015",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
        ],
        multiple=True,
    )
    @normalize(
        "leadtime_hour",
        [
            "1008",
            "1032",
            "1056",
            "1080",
            "1104",
            "1128",
            "1152",
            "1176",
            "120",
            "1200",
            "1224",
            "1248",
            "1272",
            "1296",
            "1320",
            "1344",
            "1368",
            "1392",
            "1416",
            "144",
            "1440",
            "1464",
            "1488",
            "1512",
            "1536",
            "1560",
            "1584",
            "1608",
            "1632",
            "1656",
            "168",
            "1680",
            "1704",
            "1728",
            "1752",
            "1776",
            "1800",
            "1824",
            "1848",
            "1872",
            "1896",
            "192",
            "1920",
            "1944",
            "1968",
            "1992",
            "2016",
            "2040",
            "2064",
            "2088",
            "2112",
            "2136",
            "216",
            "2160",
            "2184",
            "2208",
            "2232",
            "2256",
            "2280",
            "2304",
            "2328",
            "2352",
            "2376",
            "24",
            "240",
            "2400",
            "2424",
            "2448",
            "2472",
            "2496",
            "2520",
            "2544",
            "2568",
            "2592",
            "2616",
            "264",
            "2640",
            "2664",
            "2688",
            "2712",
            "2736",
            "2760",
            "2784",
            "2808",
            "2832",
            "2856",
            "288",
            "2880",
            "2904",
            "2928",
            "2952",
            "2976",
            "3000",
            "3024",
            "3048",
            "3072",
            "3096",
            "312",
            "3120",
            "3144",
            "3168",
            "3192",
            "3216",
            "3240",
            "3264",
            "3288",
            "3312",
            "3336",
            "336",
            "3360",
            "3384",
            "3408",
            "3432",
            "3456",
            "3480",
            "3504",
            "3528",
            "3552",
            "3576",
            "360",
            "3600",
            "3624",
            "3648",
            "3672",
            "3696",
            "3720",
            "3744",
            "3768",
            "3792",
            "3816",
            "384",
            "3840",
            "3864",
            "3888",
            "3912",
            "3936",
            "3960",
            "3984",
            "4008",
            "4032",
            "4056",
            "408",
            "4080",
            "4104",
            "4128",
            "4152",
            "4176",
            "4200",
            "4224",
            "4248",
            "4272",
            "4296",
            "432",
            "4320",
            "4344",
            "4368",
            "4392",
            "4416",
            "4440",
            "4464",
            "4488",
            "4512",
            "4536",
            "456",
            "4560",
            "4584",
            "4608",
            "4632",
            "4656",
            "4680",
            "4704",
            "4728",
            "4752",
            "4776",
            "48",
            "480",
            "4800",
            "4824",
            "4848",
            "4872",
            "4896",
            "4920",
            "4944",
            "4968",
            "4992",
            "5016",
            "504",
            "5040",
            "5064",
            "5088",
            "5112",
            "5136",
            "5160",
            "528",
            "552",
            "576",
            "600",
            "624",
            "648",
            "672",
            "696",
            "72",
            "720",
            "744",
            "768",
            "792",
            "816",
            "840",
            "864",
            "888",
            "912",
            "936",
            "96",
            "960",
            "984",
        ],
        multiple=True,
    )
    @normalize(
        "soil_level",
        [
            "1",
            "2",
            "3",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "elevation",
            "field_capacity",
            "river_discharge_in_the_last_24_hours",
            "snow_depth_water_equivalent",
            "soil_depth",
            "upstream_area",
            "volumetric_soil_moisture",
            "wilting_point",
        ],
    )
    @normalize(
        "model_levels",
        [
            "soil_levels",
            "surface_level",
        ],
    )
    @normalize(
        "format_",
        [
            "grib.zip",
            "netcdf4.zip",
        ],
    )
    def __init__(
        self,
        hmonth,
        hyear,
        leadtime_hour,
        soil_level,
        variable,
        model_levels,
        format_,
    ):
        super().__init__(
            hmonth=hmonth,
            hyear=hyear,
            leadtime_hour=leadtime_hour,
            soil_level=soil_level,
            variable=variable,
            model_levels=model_levels,
            format_=format_,
        )
