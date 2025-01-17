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


class reanalysis_uerra_europe_pressure_levels(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_UERRA_EUROPE_PRESSURE_LEVELS"
    dataset = "EO:ECMWF:DAT:REANALYSIS_UERRA_EUROPE_PRESSURE_LEVELS"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "time",
        "year",
        "pressure_level",
        "month",
        "day",
    ]

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
            "09",
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
        "month",
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
        "pressure_level",
        [
            "10",
            "100",
            "1000",
            "150",
            "20",
            "200",
            "250",
            "30",
            "300",
            "400",
            "50",
            "500",
            "600",
            "70",
            "700",
            "750",
            "800",
            "825",
            "850",
            "875",
            "900",
            "925",
            "950",
            "975",
        ],
        multiple=True,
    )
    @normalize(
        "time",
        [
            "00:00",
            "06:00",
            "12:00",
            "18:00",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1961",
            "1962",
            "1963",
            "1964",
            "1965",
            "1966",
            "1967",
            "1968",
            "1969",
            "1970",
            "1971",
            "1972",
            "1973",
            "1974",
            "1975",
            "1976",
            "1977",
            "1978",
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
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "geopotential",
            "geopotential_height",
            "relative_humidity",
            "temperature",
            "u_component_of_wind",
            "v_component_of_wind",
        ],
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    def __init__(
        self,
        day,
        month,
        pressure_level,
        time,
        year,
        variable,
        format_,
    ):
        super().__init__(
            day=day,
            month=month,
            pressure_level=pressure_level,
            time=time,
            year=year,
            variable=variable,
            format_=format_,
        )
