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


class satellite_soil_moisture(Main):
    name = "EO:ECMWF:DAT:SATELLITE_SOIL_MOISTURE"
    dataset = "EO:ECMWF:DAT:SATELLITE_SOIL_MOISTURE"

    choices = [
        "format_",
    ]

    string_selects = [
        "variable",
        "time_aggregation",
        "version",
        "year",
        "month",
        "day",
        "type_of_record",
        "type_of_sensor",
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
        "time_aggregation",
        [
            "10_day_average",
            "day_average",
            "month_average",
        ],
        multiple=True,
    )
    @normalize(
        "type_of_record",
        [
            "cdr",
            "icdr",
        ],
        multiple=True,
    )
    @normalize(
        "type_of_sensor",
        [
            "active",
            "combined_passive_and_active",
            "passive",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "surface_soil_moisture",
            "volumetric_surface_soil_moisture",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "v201706",
            "v201812",
            "v201912",
            "v202012",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
            "2020",
            "2021",
            "2022",
            "2023",
        ],
        multiple=True,
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
        day,
        month,
        time_aggregation,
        type_of_record,
        type_of_sensor,
        variable,
        version,
        year,
        format_,
    ):
        super().__init__(
            day=day,
            month=month,
            time_aggregation=time_aggregation,
            type_of_record=type_of_record,
            type_of_sensor=type_of_sensor,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
        )
