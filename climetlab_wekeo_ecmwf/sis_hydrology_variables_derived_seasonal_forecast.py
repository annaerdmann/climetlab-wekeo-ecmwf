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


class sis_hydrology_variables_derived_seasonal_forecast(Main):
    name = "EO:ECMWF:DAT:SIS_HYDROLOGY_VARIABLES_DERIVED_SEASONAL_FORECAST"
    dataset = "EO:ECMWF:DAT:SIS_HYDROLOGY_VARIABLES_DERIVED_SEASONAL_FORECAST"

    choices = [
        "format_",
    ]

    string_selects = [
        "variable",
        "year",
        "month",
        "hydrological_model",
        "version",
    ]

    @normalize(
        "hydrological_model",
        [
            "e_hypecatch_m00",
            "e_hypecatch_m01",
            "e_hypecatch_m02",
            "e_hypecatch_m05",
            "e_hypecatch_m06",
            "e_hypecatch_m07",
            "e_hypecatch_m08",
            "e_hypecatch_m09",
            "e_hypegrid",
            "lisflood_efas",
            "vic_wur",
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
        "variable",
        [
            "brier_skill_score_above_normal_conditions",
            "brier_skill_score_below_normal_conditions",
            "continuous_ranked_probability_skill_score",
            "fair_ranked_probability_skill_score",
            "reference_river_discharge_lower_tercile",
            "reference_river_discharge_upper_tercile",
            "river_discharge",
        ],
        multiple=True,
    )
    @normalize(
        "version",
        [
            "1",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
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
        hydrological_model,
        month,
        variable,
        version,
        year,
        format_,
    ):
        super().__init__(
            hydrological_model=hydrological_model,
            month=month,
            variable=variable,
            version=version,
            year=year,
            format_=format_,
        )
