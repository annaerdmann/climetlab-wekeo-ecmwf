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


class reanalysis_era5_land(Main):
    name = "EO:ECMWF:DAT:REANALYSIS_ERA5_LAND"
    dataset = "EO:ECMWF:DAT:REANALYSIS_ERA5_LAND"

    choices = [
        "year",
        "month",
        "format_",
    ]

    string_selects = [
        "time",
        "day",
        "variable",
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
        "time",
        [
            "00:00",
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "2m_dewpoint_temperature",
            "2m_temperature",
            "evaporation_from_bare_soil",
            "evaporation_from_open_water_surfaces_excluding_oceans",
            "evaporation_from_the_top_of_canopy",
            "evaporation_from_vegetation_transpiration",
            "forecast_albedo",
            "lake_bottom_temperature",
            "lake_ice_depth",
            "lake_ice_temperature",
            "lake_mix_layer_depth",
            "lake_mix_layer_temperature",
            "lake_shape_factor",
            "lake_total_layer_temperature",
            "leaf_area_index_high_vegetation",
            "leaf_area_index_low_vegetation",
            "potential_evaporation",
            "runoff",
            "skin_reservoir_content",
            "skin_temperature",
            "snow_albedo",
            "snow_cover",
            "snow_density",
            "snow_depth",
            "snow_depth_water_equivalent",
            "snow_evaporation",
            "snowfall",
            "snowmelt",
            "soil_temperature_level_1",
            "soil_temperature_level_2",
            "soil_temperature_level_3",
            "soil_temperature_level_4",
            "sub_surface_runoff",
            "surface_latent_heat_flux",
            "surface_net_solar_radiation",
            "surface_net_thermal_radiation",
            "surface_pressure",
            "surface_runoff",
            "surface_sensible_heat_flux",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation_downwards",
            "temperature_of_snow_layer",
            "total_evaporation",
            "total_precipitation",
            "volumetric_soil_water_layer_1",
            "volumetric_soil_water_layer_2",
            "volumetric_soil_water_layer_3",
            "volumetric_soil_water_layer_4",
        ],
        multiple=True,
    )
    @normalize(
        "year",
        [
            "1950",
            "1951",
            "1952",
            "1953",
            "1954",
            "1955",
            "1956",
            "1957",
            "1958",
            "1959",
            "1960",
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
            "2020",
            "2021",
            "2022",
            "2023",
        ],
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
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
            "netcdf.zip",
        ],
    )
    @normalize("area", "bounding-box(list)")
    def __init__(
        self,
        day,
        time,
        variable,
        year,
        month,
        format_,
        area=None,
    ):
        super().__init__(
            day=day,
            time=time,
            variable=variable,
            year=year,
            month=month,
            format_=format_,
            area=area,
        )
