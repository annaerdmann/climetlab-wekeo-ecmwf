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


class cams_global_atmospheric_composition_forecasts(Main):
    name = "EO:ECMWF:DAT:CAMS_GLOBAL_ATMOSPHERIC_COMPOSITION_FORECASTS"
    dataset = "EO:ECMWF:DAT:CAMS_GLOBAL_ATMOSPHERIC_COMPOSITION_FORECASTS"

    choices = [
        "format_",
    ]

    string_selects = [
        "time",
        "leadtime_hour",
        "variable",
        "model_level",
        "type",
        "pressure_level",
    ]

    @normalize(
        "leadtime_hour",
        [
            "0",
            "1",
            "10",
            "100",
            "101",
            "102",
            "103",
            "104",
            "105",
            "106",
            "107",
            "108",
            "109",
            "11",
            "110",
            "111",
            "112",
            "113",
            "114",
            "115",
            "116",
            "117",
            "118",
            "119",
            "12",
            "120",
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
            "61",
            "62",
            "63",
            "64",
            "65",
            "66",
            "67",
            "68",
            "69",
            "7",
            "70",
            "71",
            "72",
            "73",
            "74",
            "75",
            "76",
            "77",
            "78",
            "79",
            "8",
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "89",
            "9",
            "90",
            "91",
            "92",
            "93",
            "94",
            "95",
            "96",
            "97",
            "98",
            "99",
        ],
        multiple=True,
    )
    @normalize(
        "time",
        [
            "00:00",
            "12:00",
        ],
        multiple=True,
    )
    @normalize(
        "type",
        [
            "forecast",
        ],
        multiple=True,
    )
    @normalize(
        "variable",
        [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "10m_wind_gust_in_the_last_3_hours",
            "2m_dewpoint_temperature",
            "2m_temperature",
            "acetone",
            "acetone_product",
            "acetonitrile",
            "aerosol_extinction_coefficient_1064nm",
            "aerosol_extinction_coefficient_355nm",
            "aerosol_extinction_coefficient_532nm",
            "aldehydes",
            "amine",
            "ammonia",
            "ammonium",
            "ammonium_aerosol_mass_mixing_ratio",
            "ammonium_aerosol_optical_depth_550nm",
            "anthropogenic_secondary_organic_aerosol_mass_mixing_ratio",
            "asymmetric_chlorine_dioxide_radical",
            "asymmetry_factor_1020nm",
            "asymmetry_factor_1064nm",
            "asymmetry_factor_1240nm",
            "asymmetry_factor_1640nm",
            "asymmetry_factor_2130nm",
            "asymmetry_factor_340nm",
            "asymmetry_factor_355nm",
            "asymmetry_factor_380nm",
            "asymmetry_factor_400nm",
            "asymmetry_factor_440nm",
            "asymmetry_factor_469nm",
            "asymmetry_factor_500nm",
            "asymmetry_factor_532nm",
            "asymmetry_factor_550nm",
            "asymmetry_factor_645nm",
            "asymmetry_factor_670nm",
            "asymmetry_factor_800nm",
            "asymmetry_factor_858nm",
            "asymmetry_factor_865nm",
            "attenuated_backscatter_due_to_aerosol_1064nm_from_ground",
            "attenuated_backscatter_due_to_aerosol_1064nm_from_top_of_atmosphere",
            "attenuated_backscatter_due_to_aerosol_355nm_from_ground",
            "attenuated_backscatter_due_to_aerosol_355nm_from_top_of_atmosphere",
            "attenuated_backscatter_due_to_aerosol_532nm_from_ground",
            "attenuated_backscatter_due_to_aerosol_532nm_from_top_of_atmosphere",
            "biogenic_secondary_organic_aerosol_mass_mixing_ratio",
            "black_carbon_aerosol_optical_depth_550nm",
            "boundary_layer_height",
            "bromine",
            "bromine_atom",
            "bromine_monochloride",
            "bromine_monoxide",
            "bromine_nitrate",
            "bromochlorodifluoromethane",
            "carbon_monoxide",
            "chlorine",
            "chlorine_atom",
            "chlorine_dioxide",
            "chlorine_monoxide",
            "chlorine_nitrate",
            "chlorodifluoromethane",
            "chloropentafluoroethane",
            "clear_sky_direct_solar_radiation_at_surface",
            "clear_sky_surface_photosynthetically_active_radiation",
            "cloud_base_height",
            "convective_available_potential_energy",
            "convective_inhibition",
            "convective_precipitation",
            "dibromomethane",
            "dichlorine_dioxide",
            "dichlorodifluoromethane",
            "dichlorotetrafluoroethane",
            "dimethyl_sulfide",
            "dinitrogen_pentoxide",
            "direct_solar_radiation",
            "downward_uv_radiation_at_the_surface",
            "dry_deposition_of_ammonium_aerosol",
            "dry_deposition_of_coarse_mode_nitrate_aerosol",
            "dry_deposition_of_dust_aerosol_0.03-0.55um",
            "dry_deposition_of_dust_aerosol_0.55-9um",
            "dry_deposition_of_dust_aerosol_9-20um",
            "dry_deposition_of_fine_mode_nitrate_aerosol",
            "dry_deposition_of_hydrophilic_black_carbon_aerosol",
            "dry_deposition_of_hydrophilic_organic_matter_aerosol",
            "dry_deposition_of_hydrophobic_black_carbon_aerosol",
            "dry_deposition_of_hydrophobic_organic_matter_aerosol",
            "dry_deposition_of_sea_salt_aerosol_0.03-0.5um",
            "dry_deposition_of_sea_salt_aerosol_0.5-5um",
            "dry_deposition_of_sea_salt_aerosol_5-20um",
            "dry_deposition_of_sulphate_aerosol",
            "dust_aerosol_0.03-0.55um_mixing_ratio",
            "dust_aerosol_0.03-0.55um_optical_depth_550nm",
            "dust_aerosol_0.55-0.9um_mixing_ratio",
            "dust_aerosol_0.55-9um_optical_depth_550nm",
            "dust_aerosol_0.9-20um_mixing_ratio",
            "dust_aerosol_9-20um_optical_depth_550nm",
            "dust_aerosol_optical_depth_550nm",
            "ethane",
            "ethanol",
            "ethene",
            "evaporation",
            "forecast_albedo",
            "formaldehyde",
            "formic_acid",
            "fraction_of_cloud_cover",
            "friction_velocity",
            "geopotential",
            "glyoxal",
            "height_of_convective_cloud_top",
            "high_cloud_cover",
            "hydrogen_bromide",
            "hydrogen_chloride",
            "hydrogen_cyanide",
            "hydrogen_fluoride",
            "hydrogen_peroxide",
            "hydroperoxy_radical",
            "hydrophilic_black_carbon_aerosol_mixing_ratio",
            "hydrophilic_black_carbon_aerosol_optical_depth_550nm",
            "hydrophilic_organic_matter_aerosol_mixing_ratio",
            "hydrophilic_organic_matter_aerosol_optical_depth_550nm",
            "hydrophobic_black_carbon_aerosol_mixing_ratio",
            "hydrophobic_black_carbon_aerosol_optical_depth_550nm",
            "hydrophobic_organic_matter_aerosol_mixing_ratio",
            "hydrophobic_organic_matter_aerosol_optical_depth_550nm",
            "hydroxyl_radical",
            "hypobromous_acid",
            "hypochlorous_acid",
            "isoprene",
            "lake_cover",
            "land_sea_mask",
            "large_scale_precipitation",
            "lead",
            "leaf_area_index_high_vegetation",
            "leaf_area_index_low_vegetation",
            "logarithm_of_surface_pressure",
            "low_cloud_cover",
            "mean_sea_level_pressure",
            "medium_cloud_cover",
            "methacrolein_mvk",
            "methacrylic_acid",
            "methane",
            "methane_sulfonic_acid",
            "methanol",
            "methyl_bromide",
            "methyl_chloride",
            "methyl_chloroform",
            "methyl_glyoxal",
            "methyl_peroxide",
            "methylperoxy_radical",
            "nitrate",
            "nitrate_aerosol_optical_depth_550nm",
            "nitrate_coarse_mode_aerosol_mass_mixing_ratio",
            "nitrate_coarse_mode_aerosol_optical_depth_550nm",
            "nitrate_fine_mode_aerosol_mass_mixing_ratio",
            "nitrate_fine_mode_aerosol_optical_depth_550nm",
            "nitrate_radical",
            "nitric_acid",
            "nitrogen_dioxide",
            "nitrogen_monoxide",
            "nitryl_chloride",
            "olefins",
            "organic_ethers",
            "organic_matter_aerosol_optical_depth_550nm",
            "organic_nitrates",
            "ozone",
            "paraffins",
            "particulate_matter_10um",
            "particulate_matter_1um",
            "particulate_matter_2.5um",
            "pernitric_acid",
            "peroxides",
            "peroxy_acetyl_radical",
            "peroxyacetyl_nitrate",
            "photosynthetically_active_radiation_at_the_surface",
            "potential_evaporation",
            "potential_vorticity",
            "precipitation_type",
            "propane",
            "propene",
            "radon",
            "relative_humidity",
            "sea_ice_cover",
            "sea_salt_aerosol_0.03-0.5um_mixing_ratio",
            "sea_salt_aerosol_0.03-0.5um_optical_depth_550nm",
            "sea_salt_aerosol_0.5-5um_mixing_ratio",
            "sea_salt_aerosol_0.5-5um_optical_depth_550nm",
            "sea_salt_aerosol_5-20um_mixing_ratio",
            "sea_salt_aerosol_5-20um_optical_depth_550nm",
            "sea_salt_aerosol_optical_depth_550nm",
            "sea_surface_temperature",
            "secondary_organic_aerosol_optical_depth_550nm",
            "sedimentation_of_ammonium_aerosol",
            "sedimentation_of_coarse_mode_nitrate_aerosol",
            "sedimentation_of_dust_aerosol_0.03-0.55um",
            "sedimentation_of_dust_aerosol_0.55-9um",
            "sedimentation_of_dust_aerosol_9-20um",
            "sedimentation_of_fine_mode_nitrate_aerosol",
            "sedimentation_of_hydrophilic_black_carbon_aerosol",
            "sedimentation_of_hydrophilic_organic_matter_aerosol",
            "sedimentation_of_hydrophobic_black_carbon_aerosol",
            "sedimentation_of_hydrophobic_organic_matter_aerosol",
            "sedimentation_of_sea_salt_aerosol_0.03-0.5um",
            "sedimentation_of_sea_salt_aerosol_0.5-5um",
            "sedimentation_of_sea_salt_aerosol_5-20um",
            "sedimentation_of_sulphate_aerosol",
            "single_scattering_albedo_1020nm",
            "single_scattering_albedo_1064nm",
            "single_scattering_albedo_1240nm",
            "single_scattering_albedo_1640nm",
            "single_scattering_albedo_2130nm",
            "single_scattering_albedo_340nm",
            "single_scattering_albedo_355nm",
            "single_scattering_albedo_380nm",
            "single_scattering_albedo_400nm",
            "single_scattering_albedo_440nm",
            "single_scattering_albedo_469nm",
            "single_scattering_albedo_500nm",
            "single_scattering_albedo_532nm",
            "single_scattering_albedo_550nm",
            "single_scattering_albedo_645nm",
            "single_scattering_albedo_670nm",
            "single_scattering_albedo_800nm",
            "single_scattering_albedo_858nm",
            "single_scattering_albedo_865nm",
            "skin_reservoir_content",
            "skin_temperature",
            "snow_albedo",
            "snow_depth",
            "specific_cloud_ice_water_content",
            "specific_cloud_liquid_water_content",
            "specific_humidity",
            "specific_rain_water_content",
            "specific_snow_water_content",
            "stratospheric_ozone_tracer",
            "sulphate_aerosol_mixing_ratio",
            "sulphate_aerosol_optical_depth_550nm",
            "sulphur_dioxide",
            "sunshine_duration",
            "surface_geopotential",
            "surface_latent_heat_flux",
            "surface_net_solar_radiation",
            "surface_net_solar_radiation_clear_sky",
            "surface_net_thermal_radiation",
            "surface_net_thermal_radiation_clear_sky",
            "surface_pressure",
            "surface_sensible_heat_flux",
            "surface_solar_radiation_downward_clear_sky",
            "surface_solar_radiation_downwards",
            "surface_thermal_radiation_downward_clear_sky",
            "surface_thermal_radiation_downwards",
            "temperature",
            "terpenes",
            "tetrachloromethane",
            "time_integrated_dry_deposition_mass_flux_of_ammonia",
            "time_integrated_dry_deposition_mass_flux_of_dinitrogen_pentoxide",
            "time_integrated_dry_deposition_mass_flux_of_nitric_acid",
            "time_integrated_dry_deposition_mass_flux_of_nitrogen_dioxide",
            "time_integrated_dry_deposition_mass_flux_of_nitrogen_monoxide",
            "time_integrated_dry_deposition_mass_flux_of_organic_nitrates",
            "time_integrated_dry_deposition_mass_flux_of_ozone",
            "time_integrated_dry_deposition_mass_flux_of_peroxyacetyl_nitrate",
            "time_integrated_dry_deposition_mass_flux_of_sulphur_dioxide",
            "time_integrated_wet_deposition_mass_flux_of_ammonia",
            "time_integrated_wet_deposition_mass_flux_of_dinitrogen_pentoxide",
            "time_integrated_wet_deposition_mass_flux_of_nitric_acid",
            "time_integrated_wet_deposition_mass_flux_of_nitrogen_dioxide",
            "time_integrated_wet_deposition_mass_flux_of_nitrogen_monoxide",
            "time_integrated_wet_deposition_mass_flux_of_organic_nitrates",
            "time_integrated_wet_deposition_mass_flux_of_peroxyacetyl_nitrate",
            "time_integrated_wet_deposition_mass_flux_of_sulphur_dioxide",
            "toa_incident_solar_radiation",
            "top_net_solar_radiation",
            "top_net_solar_radiation_clear_sky",
            "top_net_thermal_radiation",
            "top_net_thermal_radiation_clear_sky",
            "total_absorption_aerosol_optical_depth_1020nm",
            "total_absorption_aerosol_optical_depth_1064nm",
            "total_absorption_aerosol_optical_depth_1240nm",
            "total_absorption_aerosol_optical_depth_1640nm",
            "total_absorption_aerosol_optical_depth_2130nm",
            "total_absorption_aerosol_optical_depth_340nm",
            "total_absorption_aerosol_optical_depth_355nm",
            "total_absorption_aerosol_optical_depth_380nm",
            "total_absorption_aerosol_optical_depth_400nm",
            "total_absorption_aerosol_optical_depth_440nm",
            "total_absorption_aerosol_optical_depth_469nm",
            "total_absorption_aerosol_optical_depth_500nm",
            "total_absorption_aerosol_optical_depth_532nm",
            "total_absorption_aerosol_optical_depth_550nm",
            "total_absorption_aerosol_optical_depth_645nm",
            "total_absorption_aerosol_optical_depth_670nm",
            "total_absorption_aerosol_optical_depth_800nm",
            "total_absorption_aerosol_optical_depth_858nm",
            "total_absorption_aerosol_optical_depth_865nm",
            "total_aerosol_optical_depth_1020nm",
            "total_aerosol_optical_depth_1064nm",
            "total_aerosol_optical_depth_1240nm",
            "total_aerosol_optical_depth_1640nm",
            "total_aerosol_optical_depth_2130nm",
            "total_aerosol_optical_depth_340nm",
            "total_aerosol_optical_depth_355nm",
            "total_aerosol_optical_depth_380nm",
            "total_aerosol_optical_depth_400nm",
            "total_aerosol_optical_depth_440nm",
            "total_aerosol_optical_depth_469nm",
            "total_aerosol_optical_depth_500nm",
            "total_aerosol_optical_depth_532nm",
            "total_aerosol_optical_depth_550nm",
            "total_aerosol_optical_depth_645nm",
            "total_aerosol_optical_depth_670nm",
            "total_aerosol_optical_depth_800nm",
            "total_aerosol_optical_depth_858nm",
            "total_aerosol_optical_depth_865nm",
            "total_cloud_cover",
            "total_column_acetone",
            "total_column_acetone_product",
            "total_column_acetonitrile",
            "total_column_aldehydes",
            "total_column_amine",
            "total_column_ammonia",
            "total_column_ammonium",
            "total_column_asymmetric_chlorine_dioxide_radical",
            "total_column_bromine",
            "total_column_bromine_atom",
            "total_column_bromine_monochloride",
            "total_column_bromine_monoxide",
            "total_column_bromine_nitrate",
            "total_column_bromochlorodifluoromethane",
            "total_column_carbon_monoxide",
            "total_column_chlorine",
            "total_column_chlorine_atom",
            "total_column_chlorine_dioxide",
            "total_column_chlorine_monoxide",
            "total_column_chlorine_nitrate",
            "total_column_chlorodifluoromethane",
            "total_column_chloropentafluoroethane",
            "total_column_cloud_ice_water",
            "total_column_cloud_liquid_water",
            "total_column_dibromomethane",
            "total_column_dichlorine_dioxide",
            "total_column_dichlorodifluoromethane",
            "total_column_dichlorotetrafluoroethane",
            "total_column_dimethyl_sulfide",
            "total_column_dinitrogen_pentoxide",
            "total_column_ethane",
            "total_column_ethanol",
            "total_column_ethene",
            "total_column_formaldehyde",
            "total_column_formic_acid",
            "total_column_glyoxal",
            "total_column_hydrogen_bromide",
            "total_column_hydrogen_chloride",
            "total_column_hydrogen_cyanide",
            "total_column_hydrogen_fluoride",
            "total_column_hydrogen_peroxide",
            "total_column_hydroperoxy_radical",
            "total_column_hydroxyl_radical",
            "total_column_hypobromous_acid",
            "total_column_hypochlorous_acid",
            "total_column_hypropo2",
            "total_column_ic3h7o2",
            "total_column_isoprene",
            "total_column_lead",
            "total_column_methacrolein_mvk",
            "total_column_methacrylic_acid",
            "total_column_methane",
            "total_column_methane_sulfonic_acid",
            "total_column_methanol",
            "total_column_methyl_bromide",
            "total_column_methyl_chloride",
            "total_column_methyl_chloroform",
            "total_column_methyl_glyoxal",
            "total_column_methyl_peroxide",
            "total_column_methylperoxy_radical",
            "total_column_nitrate",
            "total_column_nitrate_radical",
            "total_column_nitric_acid",
            "total_column_nitrogen_dioxide",
            "total_column_nitrogen_monoxide",
            "total_column_nitrogen_oxides_transp",
            "total_column_nitryl_chloride",
            "total_column_no_to_alkyl_nitrate_operator",
            "total_column_no_to_no2_operator",
            "total_column_olefins",
            "total_column_organic_ethers",
            "total_column_organic_nitrates",
            "total_column_ozone",
            "total_column_paraffins",
            "total_column_pernitric_acid",
            "total_column_peroxides",
            "total_column_peroxy_acetyl_radical",
            "total_column_peroxyacetyl_nitrate",
            "total_column_polar_stratospheric_cloud",
            "total_column_propane",
            "total_column_propene",
            "total_column_radon",
            "total_column_rain_water",
            "total_column_snow_water",
            "total_column_source_of_ammonium_aerosol",
            "total_column_source_of_coarse_mode_nitrate_aerosol",
            "total_column_source_of_dust_aerosol_0.03-0.55um",
            "total_column_source_of_dust_aerosol_0.55-9um",
            "total_column_source_of_dust_aerosol_9-20um",
            "total_column_source_of_fine_mode_nitrate_aerosol",
            "total_column_source_of_hydrophilic_black_carbon_aerosol",
            "total_column_source_of_hydrophilic_organic_matter_aerosol",
            "total_column_source_of_hydrophobic_black_carbon_aerosol",
            "total_column_source_of_hydrophobic_organic_matter_aerosol",
            "total_column_source_of_sea_salt_aerosol_0.03-0.5um",
            "total_column_source_of_sea_salt_aerosol_0.5-5um",
            "total_column_source_of_sea_salt_aerosol_5-20um",
            "total_column_source_of_sulphate_aerosol",
            "total_column_stratospheric_ozone",
            "total_column_sulphur_dioxide",
            "total_column_supercooled_liquid_water",
            "total_column_terpenes",
            "total_column_tetrachloromethane",
            "total_column_tribromomethane",
            "total_column_trichlorofluoromethane",
            "total_column_trichlorotrifluoroethane",
            "total_column_trifluorobromomethane",
            "total_column_water",
            "total_column_water_vapour",
            "total_column_water_vapour_chemistry",
            "total_fine_mode_aerosol_optical_depth_1020nm",
            "total_fine_mode_aerosol_optical_depth_1064nm",
            "total_fine_mode_aerosol_optical_depth_1240nm",
            "total_fine_mode_aerosol_optical_depth_1640nm",
            "total_fine_mode_aerosol_optical_depth_2130nm",
            "total_fine_mode_aerosol_optical_depth_340nm",
            "total_fine_mode_aerosol_optical_depth_355nm",
            "total_fine_mode_aerosol_optical_depth_380nm",
            "total_fine_mode_aerosol_optical_depth_400nm",
            "total_fine_mode_aerosol_optical_depth_440nm",
            "total_fine_mode_aerosol_optical_depth_469nm",
            "total_fine_mode_aerosol_optical_depth_500nm",
            "total_fine_mode_aerosol_optical_depth_532nm",
            "total_fine_mode_aerosol_optical_depth_550nm",
            "total_fine_mode_aerosol_optical_depth_645nm",
            "total_fine_mode_aerosol_optical_depth_670nm",
            "total_fine_mode_aerosol_optical_depth_800nm",
            "total_fine_mode_aerosol_optical_depth_858nm",
            "total_fine_mode_aerosol_optical_depth_865nm",
            "total_precipitation",
            "total_sky_direct_solar_radiation_at_surface",
            "tribromomethane",
            "trichlorofluoromethane",
            "trichlorotrifluoroethane",
            "trifluorobromomethane",
            "u_component_of_wind",
            "uv_biologically_effective_dose",
            "uv_biologically_effective_dose_clear_sky",
            "v_component_of_wind",
            "vertical_velocity",
            "vertically_integrated_mass_of_ammonium_aerosol",
            "vertically_integrated_mass_of_coarse_mode_nitrate_aerosol",
            "vertically_integrated_mass_of_dust_aerosol_0.03-0.55um",
            "vertically_integrated_mass_of_dust_aerosol_0.55-9um",
            "vertically_integrated_mass_of_dust_aerosol_9-20um",
            "vertically_integrated_mass_of_fine_mode_nitrate_aerosol",
            "vertically_integrated_mass_of_hydrophilic_black_carbon_aerosol",
            "vertically_integrated_mass_of_hydrophilic_organic_matter_aerosol",
            "vertically_integrated_mass_of_hydrophobic_black_carbon_aerosol",
            "vertically_integrated_mass_of_hydrophobic_organic_matter_aerosol",
            "vertically_integrated_mass_of_sea_salt_aerosol_0.03-0.5um",
            "vertically_integrated_mass_of_sea_salt_aerosol_0.5-5um",
            "vertically_integrated_mass_of_sea_salt_aerosol_5-20um",
            "vertically_integrated_mass_of_sulphate_aerosol",
            "vertically_integrated_moisture_divergence",
            "visibility",
            "water_vapour_chemistry",
            "wet_deposition_of_ammonium_aerosol_by_convective_precipitation",
            "wet_deposition_of_ammonium_aerosol_by_large_scale_precipitation",
            "wet_deposition_of_coarse_mode_nitrate_aerosol_by_convective_precipitation",
            "wet_deposition_of_coarse_mode_nitrate_aerosol_by_large_scale_precipitation",
            "wet_deposition_of_dust_aerosol_0.03-0.55um_by_convective_precipitation",
            "wet_deposition_of_dust_aerosol_0.03-0.55um_by_large_scale_precipitation",
            "wet_deposition_of_dust_aerosol_0.55-9um_by_convective_precipitation",
            "wet_deposition_of_dust_aerosol_0.55-9um_by_large_scale_precipitation",
            "wet_deposition_of_dust_aerosol_9-20um_by_convective_precipitation",
            "wet_deposition_of_dust_aerosol_9-20um_by_large_scale_precipitation",
            "wet_deposition_of_fine_mode_nitrate_aerosol_by_convective_precipitation",
            "wet_deposition_of_fine_mode_nitrate_aerosol_by_large_scale_precipitation",
            "wet_deposition_of_hydrophilic_black_carbon_aerosol_by_convective_precipitation",
            "wet_deposition_of_hydrophilic_black_carbon_aerosol_by_large_scale_precipitation",
            "wet_deposition_of_hydrophilic_organic_matter_aerosol_by_convective_precipitation",
            "wet_deposition_of_hydrophilic_organic_matter_aerosol_by_large_scale_precipitation",
            "wet_deposition_of_hydrophobic_black_carbon_aerosol_by_convective_precipitation",
            "wet_deposition_of_hydrophobic_black_carbon_aerosol_by_large_scale_precipitation",
            "wet_deposition_of_hydrophobic_organic_matter_aerosol_by_convective_precipitation",
            "wet_deposition_of_hydrophobic_organic_matter_aerosol_by_large_scale_precipitation",
            "wet_deposition_of_sea_salt_aerosol_0.03-0.5um_by_convective_precipitation",
            "wet_deposition_of_sea_salt_aerosol_0.03-0.5um_by_large_scale_precipitation",
            "wet_deposition_of_sea_salt_aerosol_0.5-5um_by_convective_precipitation",
            "wet_deposition_of_sea_salt_aerosol_0.5-5um_by_large_scale_precipitation",
            "wet_deposition_of_sea_salt_aerosol_5-20um_by_convective_precipitation",
            "wet_deposition_of_sea_salt_aerosol_5-20um_by_large_scale_precipitation",
            "wet_deposition_of_sulphate_aerosol_by_convective_precipitation",
            "wet_deposition_of_sulphate_aerosol_by_large_scale_precipitation",
        ],
        multiple=True,
    )
    @normalize(
        "format_",
        [
            "grib",
            "netcdf_zip",
        ],
    )
    @normalize("area", "bounding-box(list)")
    @normalize(
        "model_level",
        [
            "1",
            "10",
            "100",
            "101",
            "102",
            "103",
            "104",
            "105",
            "106",
            "107",
            "108",
            "109",
            "11",
            "110",
            "111",
            "112",
            "113",
            "114",
            "115",
            "116",
            "117",
            "118",
            "119",
            "12",
            "120",
            "121",
            "122",
            "123",
            "124",
            "125",
            "126",
            "127",
            "128",
            "129",
            "13",
            "130",
            "131",
            "132",
            "133",
            "134",
            "135",
            "136",
            "137",
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
            "61",
            "62",
            "63",
            "64",
            "65",
            "66",
            "67",
            "68",
            "69",
            "7",
            "70",
            "71",
            "72",
            "73",
            "74",
            "75",
            "76",
            "77",
            "78",
            "79",
            "8",
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "89",
            "9",
            "90",
            "91",
            "92",
            "93",
            "94",
            "95",
            "96",
            "97",
            "98",
            "99",
        ],
        multiple=True,
    )
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
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        leadtime_hour,
        time,
        type,
        variable,
        format_,
        area=None,
        model_level=None,
        pressure_level=None,
        start="2015-01-01",
        end="2023-08-03",
    ):
        super().__init__(
            leadtime_hour=leadtime_hour,
            time=time,
            type=type,
            variable=variable,
            format_=format_,
            area=area,
            model_level=model_level,
            pressure_level=pressure_level,
            start=start,
            end=end,
        )
