import math
from typing import List

# Returns [real relative permittivity, imaginary relative permittivity] of a
# soil - water mixture. 
def soil_peplinski_1995(
        _frequency: float,  # Hz
        _moisture_volumetric_ratio: float,  # unitless ratio
        _sand_mass_fraction: float,  # unitless ratio
        _clay_mass_fraction: float,  # unitless ratio
        _density_specific: float,  # g / cm^3
        _density_bulk: float  # g / cm^3
):
    # Soil mixing model for 300MHz to 6GHz for wet soils composed of clay,
    # sand, and silt. Equations  from [1]. The output effective imaginary
    # permittivity is the imaginary permittivity + conductivity / omega.

    # References
    # [1]   N. Peplinski, F. Ulaby, and M. Dobson, “Dielectric properties of
    #       soils in the 0.3-1.3-GHz range,” IEEE Transactions on Geoscience
    #       and Remote Sensing, vol. 33, pp. 803–807, May 1995.
    # [2]   F. T. Ulaby, R. K. Moore, and A. K. Fung, Microwave Remote Sensing,
    #       vol. 3. Dedham, MA: Artech House, 1986, Appendix E.
    # [3]   M. C. Dobson, F. T. Ulaby, M. T. Hallikainen, and M. A. El-Rayes,
    #       “Microwave dielectric behavior of wet soil, Part II: Dielectric mixing
    #       models,” IEEE Trans. Geosci. Remote Sensing, vol. GRS-23, pp. 3546,
    #       Jan. 1985.

    _permittivity_free_space = 8.85418782e-12
    _permittivity_water_low_freq_limit = 80.1  # at room temperature based on [2]
    _permittivity_water_high_freq_limit = 4.9
    _relaxation_time_water = 0.58e-10 / (2 * math.pi)  #
    _alpha_coeff = 0.65  # empirically determined constant

    _conductivity_effective = 0.0467 + 0.2204 * _density_bulk - 0.4111 * _sand_mass_fraction \
        + 0.6614 * _clay_mass_fraction # [1] eq.10

    _permittivity_rel_real_free_water = _permittivity_water_high_freq_limit \
        + (_permittivity_water_low_freq_limit - _permittivity_water_high_freq_limit) \
        / (1 + (2 * math.pi * _frequency * _relaxation_time_water) ** 2) # [1] eq.6

    _term_1 = (2 * math.pi * _frequency * _relaxation_time_water) \
        * (_permittivity_water_low_freq_limit - _permittivity_water_high_freq_limit) \
        / (1 + (2 * math.pi * _frequency * _relaxation_time_water) ** 2)

    _term_2 = (_conductivity_effective * (_density_specific - _density_bulk)) \
        / (2 * math.pi * _permittivity_free_space * _frequency * _density_specific \
           * _moisture_volumetric_ratio)

    _permittivity_rel_imag_free_water = _term_1 + _term_2 # [1] eq.7

    _beta_real_coeff = 1.2748 - 0.519 * _sand_mass_fraction - 0.152 * _clay_mass_fraction # [1] eq.4

    _beta_imag_coeff = 1.33797 - 0.603 * _sand_mass_fraction - 0.166 * _clay_mass_fraction # [1] eq.5

    _permittivity_rel_dry_soil = (1.01 + 0.44 * _density_specific) ** 2 - 0.062 # [3] eq.22

    _permittivity_rel_real_soil_mixture = (1 + _density_bulk / _density_specific \
         * _permittivity_rel_dry_soil ** _alpha_coeff + _moisture_volumetric_ratio ** _beta_real_coeff \
         * _permittivity_rel_real_free_water ** _alpha_coeff - _moisture_volumetric_ratio) \
         ** (1 / _alpha_coeff) # [1] eq.2

    _permittivity_rel_real_soil_mixture = 1.15*_permittivity_rel_real_soil_mixture -0.68 # [1] eq.9

    _permittivity_rel_imag_soil_mixture = (_moisture_volumetric_ratio ** _beta_imag_coeff \
         * _permittivity_rel_imag_free_water ** _alpha_coeff) ** (1 / _alpha_coeff) # [1] eq.3
    
    return [_permittivity_rel_real_soil_mixture, _permittivity_rel_imag_soil_mixture]
