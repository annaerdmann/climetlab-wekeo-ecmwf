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


class sis_temperature_statistics(Main):
    name = "EO:ECMWF:DAT:SIS_TEMPERATURE_STATISTICS"
    dataset = "EO:ECMWF:DAT:SIS_TEMPERATURE_STATISTICS"

    choices = [
        "variable",
        "period",
        "format_",
    ]

    string_selects = [
        "ensemble_statistic",
        "statistic",
        "experiment",
    ]

    @normalize(
        "ensemble_statistic",
        [
            "ensemble_members_average",
            "ensemble_members_standard_deviation",
        ],
        multiple=True,
    )
    @normalize(
        "experiment",
        [
            "rcp4_5",
            "rcp8_5",
        ],
        multiple=True,
    )
    @normalize(
        "statistic",
        [
            "10th_percentile",
            "1st_percentile",
            "25th_percentile",
            "50th_percentile",
            "5th_percentile",
            "75th_percentile",
            "90th_percentile",
            "95th_percentile",
            "97th_percentile",
            "99th_percentile",
            "time_average",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "average_temperature",
            "maximum_temperature",
            "minimum_temperature",
        ],
    )
    @normalize(
        "period",
        [
            "summer",
            "winter",
            "year",
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
        ensemble_statistic,
        experiment,
        statistic,
        variable,
        period,
        format_,
    ):
        super().__init__(
            ensemble_statistic=ensemble_statistic,
            experiment=experiment,
            statistic=statistic,
            variable=variable,
            period=period,
            format_=format_,
        )
