import math
import matplotlib as plt
import numpy as np


def alpha_beta(_permittivity_rel_real: float, _permittivity_rel_imag: float, _frequency: float):
    _permittivity_free_space = 8.85418782e-12
    _permeability_free_space = 1.25663706e-6

    _alpha = _frequency * 2 * math.pi * (_permeability_free_space * _permittivity_free_space
                                         * _permittivity_rel_real / 2 * (
                                                 np.sqrt(1 + (_permittivity_rel_imag / _permittivity_rel_real) ** 2)
                                                 - 1)) ** 0.5
    _beta = _frequency * 2 * math.pi * (_permeability_free_space * _permittivity_free_space
                                        * _permittivity_rel_real / 2 * (
                                                np.sqrt(1 + (_permittivity_rel_imag / _permittivity_rel_real) ** 2)
                                                + 1)) ** 0.5
    return [_alpha, _beta]


def power_loss_db(_alpha: float, _distance: float):
    return 20 * math.log10(math.exp(-_alpha * _distance))


def velocity(_beta: float, _frequency: float):
    return 2 * math.pi * _frequency / _beta


def range_resolution(_beta: float, _frequency: float, _bandwidth: float):
    _velocity = velocity(_beta, _frequency)
    return _velocity / (2 * _bandwidth)
