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


class cams_europe_air_quality_reanalyses(Main):
    name = "EO:ECMWF:DAT:CAMS_EUROPE_AIR_QUALITY_REANALYSES"
    dataset = "EO:ECMWF:DAT:CAMS_EUROPE_AIR_QUALITY_REANALYSES"

    choices = [
        "format_",
    ]

    string_selects = [
        "level",
        "variable",
        "year",
        "type",
        "month",
        "model",
    ]

    @normalize(
        "level",
        [
            "0",
            "100",
            "1000",
            "2000",
            "250",
            "3000",
            "50",
            "500",
            "5000",
            "750",
        ],
        multiple=True,
    )
    @normalize(
        "model",
        [
            "chimere",
            "dehm",
            "emep",
            "ensemble",
            "euradim",
            "gemaq",
            "lotos",
            "match",
            "minni",
            "mocage",
            "silam",
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
        "type",
        [
            "interim_reanalysis",
            "validated_reanalysis",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "ammonia",
            "carbon_monoxide",
            "dust",
            "nitrogen_dioxide",
            "nitrogen_monoxide",
            "non_methane_vocs",
            "ozone",
            "particulate_matter_10um",
            "particulate_matter_2.5um",
            "peroxyacyl_nitrates",
            "pm10_wildfires",
            "residential_elementary_carbon",
            "secondary_inorganic_aerosol",
            "sulphur_dioxide",
            "total_elementary_carbon",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "2018",
            "2019",
            "2020",
            "2021",
            "2022",
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
        level,
        model,
        month,
        type,
        variable,
        year,
        format_,
    ):
        super().__init__(
            level=level,
            model=model,
            month=month,
            type=type,
            variable=variable,
            year=year,
            format_=format_,
        )
