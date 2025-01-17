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


class sis_urban_climate_cities(Main):
    name = "EO:ECMWF:DAT:SIS_URBAN_CLIMATE_CITIES"
    dataset = "EO:ECMWF:DAT:SIS_URBAN_CLIMATE_CITIES"

    choices = [
        "variable",
        "format_",
    ]

    string_selects = [
        "month",
        "year",
        "city",
    ]

    @normalize(
        "city",
        [
            "alicante",
            "amsterdam",
            "antwerp",
            "athens",
            "barcelona",
            "bari",
            "basel",
            "belgrade",
            "berlin",
            "bilbao",
            "birmingham",
            "bologna",
            "bordeaux",
            "brasov",
            "bratislava",
            "brussels",
            "bucharest",
            "budapest",
            "charleroi",
            "cluj_napoca",
            "cologne",
            "copenhagen",
            "cracow",
            "debrecen",
            "dublin",
            "dusseldorf",
            "edinburgh",
            "frankfurt",
            "gdansk",
            "geneva",
            "genoa",
            "ghent",
            "glasgow",
            "goteborg",
            "graz",
            "gyor",
            "hamburg",
            "helsinki",
            "klaipeda",
            "kosice",
            "leeds",
            "leipzig",
            "liege",
            "lille",
            "lisbon",
            "ljubljana",
            "lodz",
            "london",
            "luxembourg",
            "lyon",
            "madrid",
            "malaga",
            "marseille",
            "milan",
            "miskolc",
            "montpellier",
            "munich",
            "murcia",
            "nantes",
            "naples",
            "newcastle",
            "nice",
            "novi_sad",
            "oslo",
            "padua",
            "palermo",
            "palma_de_mallorca",
            "paris",
            "pecs",
            "podgorica",
            "porto",
            "prague",
            "reykjavik",
            "riga",
            "rome",
            "rotterdam",
            "sarajevo",
            "sevilla",
            "skopje",
            "sofia",
            "split",
            "stockholm",
            "strasbourg",
            "szeged",
            "tallinn",
            "tartu",
            "thessaloniki",
            "tirana",
            "toulouse",
            "trieste",
            "turin",
            "utrecht",
            "valencia",
            "varna",
            "vienna",
            "vilnius",
            "warsaw",
            "wroclaw",
            "zagreb",
            "zurich",
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
        "year",
        [
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
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "air_temperature",
            "land_sea_mask",
            "relative_humidity",
            "rural_urban_mask",
            "specific_humidity",
            "wind_speed",
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
        city,
        month,
        year,
        variable,
        format_,
    ):
        super().__init__(
            city=city,
            month=month,
            year=year,
            variable=variable,
            format_=format_,
        )
