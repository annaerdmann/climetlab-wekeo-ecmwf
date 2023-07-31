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


class cams_global_ghg_reanalysis_egg4(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_GHG_REANALYSIS_EGG4"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_GHG_REANALYSIS_EGG4"

    choices = [
        "format_",
    ]

    string_selects = [
        "variable",
        "variable",
        "variable",
        "variable",
        "variable",
        "variable",
        "pressure_level",
        "model_level",
        "step",
    ]

    @normalize(
        "variable",
        [
            "downward_uv_radiation_at_the_surface",
            "forecast_albedo",
            "photosynthetically_active_radiation_at_the_surface",
            "snow_albedo",
            "sunshine_duration",
            "surface_net_solar_radiation",
            "surface_net_solar_radiation_clear_sky",
            "surface_net_thermal_radiation",
            "surface_net_thermal_radiation_clear_sky",
            "surface_solar_radiation_downward_clear_sky",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation_downward_clear_sky",
            "surface_thermal_radiation_downwards",
            "toa_incident_solar_radiation",
            "top_net_solar_radiation",
            "top_net_solar_radiation_clear_sky",
            "top_net_thermal_radiation",
            "top_net_thermal_radiation_clear_sky",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "ch4_column_mean_molar_fraction",
            "co2_column_mean_molar_fraction",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "accumulated_carbon_dioxide_ecosystem_respiration",
            "accumulated_carbon_dioxide_gross_primary_production",
            "accumulated_carbon_dioxide_net_ecosystem_exchange",
            "anthropogenic_emissions_of_carbon_dioxide",
            "flux_of_carbon_dioxide_ecosystem_respiration",
            "flux_of_carbon_dioxide_gross_primary_production",
            "flux_of_carbon_dioxide_net_ecosystem_exchange",
            "gpp_coefficient_from_biogenic_flux_adjustment_system",
            "methane_loss_rate_due_to_radical_hydroxyl_oh",
            "methane_surface_fluxes",
            "ocean_flux_of_carbon_dioxide",
            "rec_coefficient_from_biogenic_flux_adjustment_system",
            "wildfire_flux_of_carbon_dioxide",
            "wildfire_flux_of_methane",
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
            "boundary_layer_height",
            "convective_available_potential_energy",
            "convective_inhibition",
            "convective_precipitation",
            "evaporation",
            "high_cloud_cover",
            "land_sea_mask",
            "large_scale_precipitation",
            "low_cloud_cover",
            "mean_sea_level_pressure",
            "medium_cloud_cover",
            "potential_evaporation",
            "precipitation_type",
            "sea_ice_cover",
            "sea_surface_temperature",
            "skin_reservoir_content",
            "skin_temperature",
            "snow_depth",
            "surface_geopotential",
            "surface_latent_heat_flux",
            "surface_sensible_heat_flux",
            "total_cloud_cover",
            "total_column_cloud_ice_water",
            "total_column_cloud_liquid_water",
            "total_column_water",
            "total_column_water_vapour",
            "total_precipitation",
            "visibility",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "carbon_dioxide",
            "methane",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "fraction_of_cloud_cover",
            "geopotential",
            "logarithm_of_surface_pressure",
            "potential_vorticity",
            "relative_humidity",
            "specific_cloud_ice_water_content",
            "specific_cloud_liquid_water_content",
            "specific_humidity",
            "specific_rain_water_content",
            "specific_snow_water_content",
            "temperature",
            "u_component_of_wind",
            "v_component_of_wind",
            "vertical_velocity",
        ],
        multiple=True,
    )
    @normalize(
        "step",
        [
            "0",
            "12",
            "15",
            "18",
            "21",
            "3",
            "6",
            "9",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf",
        ],
    )
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "pressure_level",
        [
            "1",
            "10",
            "100",
            "1000",
            "150",
            "2",
            "20",
            "200",
            "250",
            "3",
            "30",
            "300",
            "400",
            "5",
            "50",
            "500",
            "600",
            "7",
            "70",
            "700",
            "800",
            "850",
            "900",
            "925",
            "950",
        ],
        multiple=True,
    )
    @normalize(
        "model_level",
        [
            "1",
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
            "2",
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
            "3",
            "30",
            "31",
            "32",
            "33",
            "34",
            "35",
            "36",
            "37",
            "38",
            "39",
            "4",
            "40",
            "41",
            "42",
            "43",
            "44",
            "45",
            "46",
            "47",
            "48",
            "49",
            "5",
            "50",
            "51",
            "52",
            "53",
            "54",
            "55",
            "56",
            "57",
            "58",
            "59",
            "6",
            "60",
            "7",
            "8",
            "9",
        ],
        multiple=True,
    )
    def __init__(
        self,
        variable,
        variable,
        variable,
        variable,
        variable,
        variable,
        step,
        format_,
        area=None,
        start="2003-01-01",
        end="2020-12-31",
        pressure_level=None,
        model_level=None,
    ):
        super().__init__(
            variable=variable,
            variable=variable,
            variable=variable,
            variable=variable,
            variable=variable,
            variable=variable,
            step=step,
            format_=format_,
            area=area,
            start=start,
            end=end,
            pressure_level=pressure_level,
            model_level=model_level,
        )
