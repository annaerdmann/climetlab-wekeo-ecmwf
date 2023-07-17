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


class sis_ecv_cmip5_bias_corrected(Main):
    name = "EO:ECMWF:DAT:SIS_ECV_CMIP5_BIAS_CORRECTED"
    dataset = "EO:ECMWF:DAT:SIS_ECV_CMIP5_BIAS_CORRECTED"

    choices = [
        "variable",
        "model",
        "experiment",
        "format_",
    ]

    string_selects = [
        "period",
        "period",
        "period",
    ]

    @normalize(
        "period",
        [
            "19500101-19741231",
            "19500101-19801231",
            "19500101-19991231",
            "19510101-19551231",
            "19560101-19601231",
            "19591201-19691130",
            "19600101-19641231",
            "19600101-19691231",
            "19610101-19651231",
            "19641201-19691130",
            "19650101-19691231",
            "19660101-19701231",
            "19691201-19741130",
            "19691201-19791130",
            "19700101-19741231",
            "19700101-19791231",
            "19710101-19751231",
            "19741201-19791130",
            "19750101-19791231",
            "19750101-19991231",
            "19750101-20051231",
            "19760101-19801231",
            "19791201-19841130",
            "19791201-19891130",
            "19800101-19841231",
            "19800101-19891231",
            "19810101-19851231",
            "19810101-20051231",
            "19841201-19891130",
            "19850101-19891231",
            "19860101-19901231",
            "19891201-19941130",
            "19891201-19991130",
            "19900101-19941231",
            "19900101-19991231",
            "19910101-19951231",
            "19941201-19991130",
            "19950101-19991231",
            "19960101-20001231",
            "19991201-20041130",
            "19991201-20051130",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "20000101-20041231",
            "20000101-20051231",
            "20010101-20051231",
            "20041201-20051130",
            "20050101-20051231",
            "20051201-20101130",
            "20051201-20151130",
            "20060101-20091231",
            "20060101-20101231",
            "20060101-20301231",
            "20060101-20501231",
            "20060101-20551231",
            "20100101-20191231",
            "20101201-20151130",
            "20110101-20151231",
            "20151201-20201130",
            "20151201-20251130",
            "20160101-20201231",
            "20200101-20291231",
            "20201201-20251130",
            "20210101-20251231",
            "20251201-20301130",
            "20251201-20351130",
            "20260101-20301231",
            "20300101-20391231",
            "20301201-20351130",
            "20310101-20351231",
            "20310101-20551231",
            "20351201-20401130",
            "20351201-20451130",
            "20360101-20401231",
            "20400101-20491231",
            "20401201-20451130",
            "20410101-20451231",
            "20451201-20501130",
            "20451201-20551130",
            "20460101-20501231",
        ],
        multiple=True,
    )
    @normalize(
        "period",
        [
            "20500101-20591231",
            "20501201-20551130",
            "20510101-20551231",
            "20510101-20951231",
            "20551201-20601130",
            "20551201-20651130",
            "20560101-20601231",
            "20560101-20801231",
            "20560101-21001231",
            "20600101-20691231",
            "20601201-20651130",
            "20610101-20651231",
            "20651201-20701130",
            "20651201-20751130",
            "20660101-20701231",
            "20700101-20791231",
            "20701201-20751130",
            "20710101-20751231",
            "20751201-20801130",
            "20751201-20851130",
            "20760101-20801231",
            "20800101-20891231",
            "20801201-20851130",
            "20810101-20851231",
            "20810101-20991231",
            "20810101-21001231",
            "20851201-20901130",
            "20851201-20951130",
            "20860101-20901231",
            "20900101-21001231",
            "20901201-20951130",
            "20910101-20951231",
            "20951201-20991130",
            "20951201-20991231",
            "20960101-20991231",
            "20960101-21001231",
            "20991201-20991231",
            "21000101-21001231",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "maximum_2m_temperature",
            "mean_2m_temperature",
            "minimum_2m_temperature",
            "precipitation_flux",
        ],
    )
    @normalize(
        "model",
        [
            "access1_0",
            "access1_3",
            "bcc_csm1_1",
            "bcc_csm1_1_m",
            "bnu_esm",
            "cnrm_cm5",
            "ec_earth",
            "gfdl_cm3",
            "gfdl_esm2g",
            "gfdl_esm2m",
            "hadgem2_cc",
            "hadgem2_es",
            "ipsl_cm5a_lr",
            "ipsl_cm5a_mr",
            "ipsl_cm5b_lr",
            "mpi_esm_lr",
            "mpi_esm_mr",
            "noresm1_m",
        ],
    )
    @normalize(
        "experiment",
        [
            "rcp_4_5",
            "rcp_8_5",
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
        period,
        period,
        period,
        variable,
        model,
        experiment,
        format_,
    ):
        super().__init__(
            period=period,
            period=period,
            period=period,
            variable=variable,
            model=model,
            experiment=experiment,
            format_=format_,
        )